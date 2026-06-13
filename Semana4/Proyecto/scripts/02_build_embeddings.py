from __future__ import annotations

import argparse
from pathlib import Path
import sys

PROJECT_ROOT = next(
    (p for p in Path(__file__).resolve().parents if (p / "src").is_dir()),
    Path(__file__).resolve().parent,
)
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

import json
import numpy as np

from src.dataset_utils import explode_all_captions, first_caption_metadata, load_metadata
from src.openclip_utils import create_model, encode_image_paths, encode_texts
from src.io_utils import ensure_dir


def _default_text_metadata_path(output_path: Path) -> Path:
    return output_path.with_suffix(".text_metadata.csv")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--metadata-csv", required=True)
    parser.add_argument("--model-name", default="ViT-B-32")
    parser.add_argument("--pretrained", default="laion2b_s34b_b79k")
    parser.add_argument("--batch-size", type=int, default=16)
    parser.add_argument("--caption-mode", choices=["first", "all"], default="first")
    parser.add_argument("--output", default="outputs/embeddings/bootstrap_embeddings.npz")
    parser.add_argument(
        "--text-metadata-csv",
        default=None,
        help="Ruta opcional para guardar las captions usadas como candidatos de texto.",
    )
    args = parser.parse_args()

    image_df = load_metadata(args.metadata_csv, root=Path(".")).reset_index(drop=True)
    if args.caption_mode == "all":
        text_df = explode_all_captions(image_df)
    else:
        text_df = first_caption_metadata(image_df)

    model, preprocess, tokenizer, device = create_model(args.model_name, args.pretrained)

    image_features = encode_image_paths(
        model,
        preprocess,
        image_df["filepath"].tolist(),
        device,
        batch_size=args.batch_size,
    )
    text_features = encode_texts(
        model,
        tokenizer,
        text_df["caption"].tolist(),
        device,
        batch_size=max(args.batch_size, 32),
    )

    out_path = Path(args.output)
    ensure_dir(out_path.parent)

    text_metadata_path = Path(args.text_metadata_csv) if args.text_metadata_csv else _default_text_metadata_path(out_path)
    ensure_dir(text_metadata_path.parent)
    text_df.to_csv(text_metadata_path, index=False)

    np.savez_compressed(
        out_path,
        image_features=image_features,
        text_features=text_features,
        image_ids=image_df["image_id"].astype(str).to_numpy(),
        text_image_ids=text_df["image_id"].astype(str).to_numpy(),
        text_captions=text_df["caption"].astype(str).to_numpy(),
        metadata_csv_path=str(Path(args.metadata_csv).resolve()),
        text_metadata_csv_path=str(text_metadata_path.resolve()),
        caption_mode=args.caption_mode,
        model_name=args.model_name,
        pretrained=args.pretrained,
        config_json=json.dumps(
            {
                "metadata_csv": str(Path(args.metadata_csv).resolve()),
                "text_metadata_csv": str(text_metadata_path.resolve()),
                "caption_mode": args.caption_mode,
                "n_images": int(len(image_df)),
                "n_texts": int(len(text_df)),
            },
            ensure_ascii=False,
        ),
    )
    print("Embeddings guardados en", out_path)
    print("Text metadata guardado en", text_metadata_path)
    print(f"Imágenes: {len(image_df)} | Textos: {len(text_df)} | caption_mode={args.caption_mode}")


if __name__ == "__main__":
    main()
