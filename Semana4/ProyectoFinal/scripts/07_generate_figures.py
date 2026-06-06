from __future__ import annotations

import json
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


EMBEDDINGS_FILE = (
    "outputs/embeddings/activitynet_clip_embeddings.npz"
)

METRICS_FILE = (
    "outputs/metrics/activitynet_retrieval_metrics.json"
)

OUTPUT_DIR = Path("outputs/figures")


def load_similarity():

    bundle = np.load(
        EMBEDDINGS_FILE,
        allow_pickle=True,
    )

    segment_features = bundle["segment_features"]
    text_features = bundle["text_features"]

    similarity = text_features @ segment_features.T

    return similarity


def plot_recall():

    with open(METRICS_FILE) as f:
        metrics = json.load(f)

    ks = ["R@1", "R@5", "R@10"]
    values = [metrics[k] for k in ks]

    plt.figure(figsize=(6, 4))

    plt.bar(ks, values)

    plt.ylabel("Recall")
    plt.title("ActivityNet Temporal Retrieval")

    plt.ylim(0, 1)

    plt.tight_layout()

    plt.savefig(
        OUTPUT_DIR / "recall_at_k.png"
    )

    plt.close()


def plot_rank_distribution(similarity):

    ranks = []

    for i in range(similarity.shape[0]):

        ranking = np.argsort(
            -similarity[i]
        )

        rank = (
            np.where(ranking == i)[0][0]
            + 1
        )

        ranks.append(rank)

    plt.figure(figsize=(7, 4))

    plt.hist(
        ranks,
        bins=20,
    )

    plt.xlabel(
        "Ranking del segmento correcto"
    )

    plt.ylabel(
        "Cantidad de consultas"
    )

    plt.title(
        "Distribucion de Rankings"
    )

    plt.tight_layout()

    plt.savefig(
        OUTPUT_DIR / "rank_distribution.png"
    )

    plt.close()


def plot_similarity_matrix(similarity):

    plt.figure(figsize=(8, 6))

    plt.imshow(
        similarity,
        aspect="auto",
    )

    plt.colorbar()

    plt.xlabel(
        "Segmentos de video"
    )

    plt.ylabel(
        "Consultas de texto"
    )

    plt.title(
        "Matriz de Similitud Texto-Video"
    )

    plt.tight_layout()

    plt.savefig(
        OUTPUT_DIR / "similarity_matrix.png"
    )

    plt.close()


def main():

    OUTPUT_DIR.mkdir(
        parents=True,
        exist_ok=True,
    )

    similarity = load_similarity()

    plot_recall()

    plot_rank_distribution(
        similarity
    )

    plot_similarity_matrix(
        similarity
    )

    print()
    print("Figuras generadas:")
    print()

    print(
        OUTPUT_DIR / "recall_at_k.png"
    )

    print(
        OUTPUT_DIR / "rank_distribution.png"
    )

    print(
        OUTPUT_DIR / "similarity_matrix.png"
    )


if __name__ == "__main__":
    main()