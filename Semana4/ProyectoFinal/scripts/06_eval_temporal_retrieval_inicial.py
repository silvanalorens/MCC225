from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np


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

    similarity = text_features @ segment_features.T

    metrics = {
        "R@1": recall_at_k(similarity, 1),
        "R@5": recall_at_k(similarity, 5),
        "R@10": recall_at_k(similarity, 10),
        "MRR": mean_reciprocal_rank(similarity),
    }

    output_path = Path(args.output_json)

    output_path.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    with open(output_path, "w") as f:
        json.dump(metrics, f, indent=2)

    print(json.dumps(metrics, indent=2))


if __name__ == "__main__":
    main()