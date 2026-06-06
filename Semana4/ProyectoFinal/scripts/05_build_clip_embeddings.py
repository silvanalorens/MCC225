from __future__ import annotations

from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parent.parent

if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

import argparse
import numpy as np
import pandas as pd

from src.openclip_utils import (
    create_model,
    encode_image_paths,
    encode_texts,
)


def main():

    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--frames-csv",
        default="data/activitynet/activitynet_frames.csv",
    )

    parser.add_argument(
        "--model-name",
        default="ViT-B-32",
    )

    parser.add_argument(
        "--pretrained",
        default="laion2b_s34b_b79k",
    )

    parser.add_argument(
        "--batch-size",
        type=int,
        default=16,
    )

    parser.add_argument(
        "--output",
        default="outputs/embeddings/activitynet_clip_embeddings.npz",
    )

    args = parser.parse_args()

    df = pd.read_csv(args.frames_csv)

    model, preprocess, tokenizer, device = create_model(
        args.model_name,
        args.pretrained,
    )

    segment_features = []
    segment_ids = []
    captions = []

    grouped = df.groupby(
        [
            "video_id",
            "segment_id",
        ]
    )

    for (video_id, segment_id), group in grouped:

        frame_paths = group["frame_path"].tolist()

        frame_embeddings = encode_image_paths(
            model,
            preprocess,
            frame_paths,
            device,
            batch_size=args.batch_size,
        )

        segment_embedding = frame_embeddings.mean(axis=0)

        segment_features.append(segment_embedding)

        segment_ids.append(
            f"{video_id}_seg{segment_id}"
        )

        captions.append(
            group.iloc[0]["caption"]
        )

    segment_features = np.vstack(segment_features)

    text_features = encode_texts(
        model,
        tokenizer,
        captions,
        device,
        batch_size=max(args.batch_size, 32),
    )

    output_path = Path(args.output)
    output_path.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    np.savez_compressed(
        output_path,
        segment_features=segment_features,
        text_features=text_features,
        segment_ids=np.array(segment_ids),
        captions=np.array(captions),
        model_name=args.model_name,
        pretrained=args.pretrained,
    )

    print()
    print("Embeddings guardados en:")
    print(output_path)

    print()
    print("Segmentos:", len(segment_ids))
    print("Textos:", len(captions))
    print("Dimensión:", segment_features.shape[1])


if __name__ == "__main__":
    main()