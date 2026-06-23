from __future__ import annotations
from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))
import argparse
from pathlib import Path
import numpy as np

from src.dataset_utils import load_metadata, build_caption_targets
from src.openclip_utils import create_model, encode_image_paths, encode_texts
from src.io_utils import ensure_dir


def main():
    p = argparse.ArgumentParser()
    p.add_argument('--metadata-csv', required=True)
    p.add_argument('--model-name', default='ViT-B-32')
    p.add_argument('--pretrained', default='laion2b_s34b_b79k')
    p.add_argument('--batch-size', type=int, default=16)
    p.add_argument('--output', default='outputs/embeddings/bootstrap_embeddings.npz')
    args = p.parse_args()

    df = load_metadata(args.metadata_csv, root=Path('.'))
    caption_df, image_to_text, text_to_image = build_caption_targets(df)
    model, preprocess, tokenizer, device = create_model(args.model_name, args.pretrained)
    image_features = encode_image_paths(model, preprocess, df['filepath'].tolist(), device, batch_size=args.batch_size)
    text_features = encode_texts(model, tokenizer, caption_df['caption'].tolist(), device, batch_size=max(args.batch_size, 32))

    out = Path(args.output)
    ensure_dir(out.parent)
    np.savez_compressed(
        out,
        image_features=image_features,
        text_features=text_features,
        image_ids=df['image_id'].astype(str).to_numpy(),
        image_paths=df['filepath'].astype(str).to_numpy(),
        caption_ids=caption_df['caption_id'].astype(str).to_numpy(),
        caption_image_indices=caption_df['image_index'].astype(np.int32).to_numpy(),
        metadata_csv_path=str(Path(args.metadata_csv).resolve()),
        model_name=args.model_name,
        pretrained=args.pretrained,
    )
    print('Saved embeddings to', out)

if __name__ == '__main__':
    main()
