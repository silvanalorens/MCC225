from __future__ import annotations
from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))
import argparse, json
from pathlib import Path
import numpy as np
import pandas as pd

from src.dataset_utils import load_metadata, build_caption_targets
from src.metrics import compute_similarity_matrix, summarize_multi_target_ranking, per_query_ranks
from src.retrieval import mine_hard_negatives
from src.io_utils import ensure_dir


def main():
    p = argparse.ArgumentParser()
    p.add_argument('--embeddings', required=True)
    p.add_argument('--metadata-csv', required=True)
    p.add_argument('--output-json', default='outputs/metrics/retrieval_metrics.json')
    p.add_argument('--per-query-csv', default='outputs/metrics/retrieval_per_query.csv')
    p.add_argument('--hard-negatives-csv', default='outputs/metrics/hard_negatives.csv')
    args = p.parse_args()

    bundle = np.load(args.embeddings, allow_pickle=True)
    image_features = bundle['image_features']
    text_features = bundle['text_features']
    df = load_metadata(args.metadata_csv, root=Path('.'))
    caption_df, image_to_text, text_to_image = build_caption_targets(df)
    sim = compute_similarity_matrix(image_features, text_features)
    text_positive = {idx: [img_idx] for idx, img_idx in text_to_image.items()}

    metrics = {
        'image_to_text': summarize_multi_target_ranking(sim, image_to_text),
        'text_to_image': summarize_multi_target_ranking(sim.T, text_positive),
        'n_images': int(image_features.shape[0]),
        'n_captions': int(text_features.shape[0]),
    }
    out_json = Path(args.output_json)
    ensure_dir(out_json.parent)
    with open(out_json, 'w', encoding='utf-8') as f:
        json.dump(metrics, f, indent=2, ensure_ascii=False)

    per_img = per_query_ranks(sim, image_to_text, df['image_id'].astype(str).tolist())
    per_txt = per_query_ranks(sim.T, text_positive, caption_df['caption_id'].astype(str).tolist())
    per_df = pd.concat([
        per_img.assign(direction='image_to_text'),
        per_txt.assign(direction='text_to_image'),
    ], ignore_index=True)
    per_path = Path(args.per_query_csv)
    ensure_dir(per_path.parent)
    per_df.to_csv(per_path, index=False)

    hard_df = mine_hard_negatives(sim, caption_df, top_n=min(15, len(df)))
    hard_path = Path(args.hard_negatives_csv)
    ensure_dir(hard_path.parent)
    hard_df.to_csv(hard_path, index=False)
    print(json.dumps(metrics, indent=2))
    print('Saved per-query ranks to', per_path)
    print('Saved hard negatives to', hard_path)

if __name__ == '__main__':
    main()
