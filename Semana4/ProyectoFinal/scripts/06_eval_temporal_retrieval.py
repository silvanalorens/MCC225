from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np
import pandas as pd

def recall_at_k(similarity, k):
    hits = 0

    for i in range(similarity.shape[0]):
        ranking = np.argsort(-similarity[i])

        if i in ranking[:k]:
            hits += 1

    return hits / similarity.shape[0]


def mean_reciprocal_rank(similarity):
    scores = []

    for i in range(similarity.shape[0]):
        ranking = np.argsort(-similarity[i])

        rank = np.where(ranking == i)[0][0] + 1

        scores.append(1.0 / rank)

    return float(np.mean(scores))

def build_top5_results(
    similarity,
    captions,
    segment_ids,
):

    rows = []

    for i in range(similarity.shape[0]):

        ranking = np.argsort(-similarity[i])

        top5 = ranking[:5]

        row = {
            "query_caption": captions[i],
            "correct_segment": segment_ids[i],
        }

        for j, idx in enumerate(top5):

            row[f"top{j+1}_segment"] = segment_ids[idx]
            row[f"top{j+1}_score"] = float(
                similarity[i, idx]
            )

        rows.append(row)

    return pd.DataFrame(rows)

def build_hard_negatives(
    similarity,
    captions,
    segment_ids,
):

    rows = []

    for i in range(similarity.shape[0]):

        ranking = np.argsort(-similarity[i])

        for idx in ranking:

            if idx != i:

                rows.append(
                    {
                        "query_caption": captions[i],
                        "correct_segment": segment_ids[i],
                        "hard_negative_segment": segment_ids[idx],
                        "similarity": float(
                            similarity[i, idx]
                        ),
                    }
                )

                break

    return pd.DataFrame(rows)

def main():

    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--embeddings",
        default="outputs/embeddings/activitynet_clip_embeddings.npz",
    )

    parser.add_argument(
        "--output-json",
        default="outputs/metrics/activitynet_retrieval_metrics.json",
    )

    args = parser.parse_args()

    bundle = np.load(
        args.embeddings,
        allow_pickle=True,
    )

    segment_features = bundle["segment_features"]
    text_features = bundle["text_features"]

    segment_ids = bundle["segment_ids"]
    captions = bundle["captions"]

    similarity = text_features @ segment_features.T

    metrics = {
        "R@1": recall_at_k(similarity, 1),
        "R@5": recall_at_k(similarity, 5),
        "R@10": recall_at_k(similarity, 10),
        "MRR": mean_reciprocal_rank(similarity),
    }

    output_json = Path(args.output_json)

    output_json.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    with open(output_json, "w") as f:
        json.dump(metrics, f, indent=2)

    top5_df = build_top5_results(
        similarity,
        captions,
        segment_ids,
    )

    top5_csv = (
        output_json.parent /
        "activitynet_top5.csv"
    )

    top5_df.to_csv(
        top5_csv,
        index=False,
    )

    hard_df = build_hard_negatives(
        similarity,
        captions,
        segment_ids,
    )

    hard_csv = (
        output_json.parent /
        "activitynet_hard_negatives.csv"
    )

    hard_df.to_csv(
        hard_csv,
        index=False,
    )

    print()
    print(json.dumps(metrics, indent=2))

    print()
    print("Top5:", top5_csv)

    print("Hard negatives:", hard_csv)


if __name__ == "__main__":
    main()