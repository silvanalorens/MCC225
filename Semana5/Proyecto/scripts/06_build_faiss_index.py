from __future__ import annotations
from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))
import argparse
from pathlib import Path
import numpy as np
import pandas as pd

from src.dataset_utils import load_metadata
from src.openclip_utils import create_model, encode_texts
from src.faiss_utils import build_index, search
from src.io_utils import ensure_dir


def main():
    p = argparse.ArgumentParser()
    p.add_argument('--embeddings', required=True)
    p.add_argument('--metadata-csv', required=True)
    p.add_argument('--queries-csv', required=True)
    p.add_argument('--output-csv', default='outputs/faiss/query_results.csv')
    p.add_argument('--top-k', type=int, default=3)
    args = p.parse_args()

    df = load_metadata(args.metadata_csv, root=Path('.'))
    queries = pd.read_csv(args.queries_csv)
    bundle = np.load(args.embeddings, allow_pickle=True)
    image_features = bundle['image_features'].astype('float32')
    model_name = str(bundle['model_name'])
    pretrained = str(bundle['pretrained'])

    model, _, tokenizer, device = create_model(model_name, pretrained)
    q_feats = encode_texts(model, tokenizer, queries['query'].astype(str).tolist(), device).astype('float32')
    index = build_index(image_features)
    scores, idxs = search(index, q_feats, k=args.top_k)
    rows = []
    for q_idx, query in enumerate(queries['query'].astype(str).tolist()):
        for rank, (score, img_idx) in enumerate(zip(scores[q_idx], idxs[q_idx]), start=1):
            row = df.iloc[int(img_idx)]
            rows.append({
                'query': query,
                'rank': rank,
                'image_id': row['image_id'],
                'filepath': row['filepath'],
                'label': row.get('label', ''),
                'caption': row['caption'],
                'score': float(score),
            })
    out = Path(args.output_csv)
    ensure_dir(out.parent)
    pd.DataFrame(rows).to_csv(out, index=False)
    print('Saved', out)

if __name__ == '__main__':
    main()
