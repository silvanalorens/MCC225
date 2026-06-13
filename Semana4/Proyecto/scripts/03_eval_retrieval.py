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
import pandas as pd

from src.dataset_utils import first_caption_metadata, load_metadata
from src.metrics import summarize_ranking_by_id
from src.retrieval import mine_hard_negatives
from src.io_utils import ensure_dir


def _scalar_string(bundle: np.lib.npyio.NpzFile, key: str, default: str = "") -> str:
    if key not in bundle:
        return default
    value = bundle[key]
    try:
        return str(value.item())
    except Exception:
        return str(value)


def _load_text_metadata(bundle: np.lib.npyio.NpzFile, image_df: pd.DataFrame) -> pd.DataFrame:
    path = _scalar_string(bundle, "text_metadata_csv_path")
    if path and Path(path).exists():
        return pd.read_csv(path)

    if "text_image_ids" in bundle and "text_captions" in bundle:
        text_image_ids = [str(x) for x in bundle["text_image_ids"].tolist()]
        text_captions = [str(x) for x in bundle["text_captions"].tolist()]
        return pd.DataFrame({
            "image_id": text_image_ids,
            "caption_id": [f"{image_id}_cap{i:02d}" for i, image_id in enumerate(text_image_ids)],
            "caption": text_captions,
        })

    return first_caption_metadata(image_df)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--embeddings", required=True)
    parser.add_argument("--metadata-csv", required=True)
    parser.add_argument("--output-json", default="outputs/metrics/retrieval_metrics.json")
    parser.add_argument("--hard-negatives-csv", default="outputs/metrics/hard_negatives.csv")
    parser.add_argument("--top-n-hard-negatives", type=int, default=10)
    args = parser.parse_args()

    bundle = np.load(args.embeddings, allow_pickle=False)
    image_features = bundle["image_features"]
    text_features = bundle["text_features"]
    sim = image_features @ text_features.T

    image_df = load_metadata(args.metadata_csv, root=Path(".")).reset_index(drop=True)
    text_df = _load_text_metadata(bundle, image_df).reset_index(drop=True)

    image_ids = [str(x) for x in (bundle["image_ids"].tolist() if "image_ids" in bundle else image_df["image_id"].tolist())]
    text_image_ids = [str(x) for x in (bundle["text_image_ids"].tolist() if "text_image_ids" in bundle else text_df["image_id"].tolist())]

    metrics = {
        "image_to_text": summarize_ranking_by_id(sim, image_ids, text_image_ids),
        "text_to_image": summarize_ranking_by_id(sim.T, text_image_ids, image_ids),
        "n_images": int(sim.shape[0]),
        "n_texts": int(sim.shape[1]),
        "caption_mode": _scalar_string(bundle, "caption_mode", default="unknown"),
    }

    out_json = Path(args.output_json)
    ensure_dir(out_json.parent)
    with open(out_json, "w", encoding="utf-8") as f:
        json.dump(metrics, f, indent=2, ensure_ascii=False)

    hard_df = mine_hard_negatives(sim, image_df, text_df, top_n=args.top_n_hard_negatives)
    hard_path = Path(args.hard_negatives_csv)
    ensure_dir(hard_path.parent)
    hard_df.to_csv(hard_path, index=False)

    print(json.dumps(metrics, indent=2, ensure_ascii=False))
    print("Negativos duros guardados en", hard_path)


if __name__ == "__main__":
    main()
