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

import numpy as np
import pandas as pd

from src.dataset_utils import first_caption_metadata, load_metadata
from src.retrieval import mine_hard_negatives


def _scalar_string(bundle: np.lib.npyio.NpzFile, key: str, default: str = "") -> str:
    if key not in bundle:
        return default
    try:
        return str(bundle[key].item())
    except Exception:
        return str(bundle[key])


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--embeddings", required=True)
    parser.add_argument("--metadata-csv", required=True)
    parser.add_argument("--text-metadata-csv", default=None)
    parser.add_argument("--top-n", type=int, default=10)
    args = parser.parse_args()

    bundle = np.load(args.embeddings, allow_pickle=False)
    sim = bundle["image_features"] @ bundle["text_features"].T
    image_df = load_metadata(args.metadata_csv, root=Path(".")).reset_index(drop=True)

    text_metadata_path = args.text_metadata_csv or _scalar_string(bundle, "text_metadata_csv_path")
    if text_metadata_path and Path(text_metadata_path).exists():
        text_df = pd.read_csv(text_metadata_path)
    else:
        text_df = first_caption_metadata(image_df)

    hard = mine_hard_negatives(sim, image_df, text_df, top_n=args.top_n)
    print(hard.to_string(index=False))


if __name__ == "__main__":
    main()
