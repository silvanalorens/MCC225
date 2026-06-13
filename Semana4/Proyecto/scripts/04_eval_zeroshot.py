
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

from src.dataset_utils import load_metadata
from src.openclip_utils import create_model, encode_texts
from src.zeroshot import build_class_prompts, predict
from src.io_utils import ensure_dir

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--embeddings", required=True)
    parser.add_argument("--metadata-csv", required=True)
    parser.add_argument("--prompt-config", required=True)
    parser.add_argument("--output-csv", default="outputs/metrics/zeroshot_predictions.csv")
    args = parser.parse_args()

    df = load_metadata(args.metadata_csv, root=Path("."))
    if "label" not in df.columns or df["label"].fillna("").eq("").all():
        raise ValueError("metadata must contain non-empty label column for zero-shot evaluation")

    with open(args.prompt_config, "r", encoding="utf-8") as f:
        prompt_cfg = json.load(f)

    bundle = np.load(args.embeddings, allow_pickle=False)
    image_features = bundle["image_features"]
    model_name = str(bundle["model_name"].item())
    pretrained = str(bundle["pretrained"].item())

    model, _, tokenizer, device = create_model(model_name, pretrained)
    internal_labels, prompts = build_class_prompts(prompt_cfg["label_map"], prompt_cfg["templates"])
    prompt_features = encode_texts(model, tokenizer, prompts, device)

    preds = predict(image_features, prompt_features, internal_labels)
    out_df = df[["image_id", "filepath", "caption", "label"]].copy()
    out_df["pred_label"] = preds
    out_df["is_correct"] = out_df["label"] == out_df["pred_label"]
    out_df["prompt_template_used"] = prompt_cfg["templates"][0]

    out_path = Path(args.output_csv)
    ensure_dir(out_path.parent)
    out_df.to_csv(out_path, index=False)
    print("Accuracy:", float(out_df["is_correct"].mean()))
    print("Guardados:", out_path)

if __name__ == "__main__":
    main()
