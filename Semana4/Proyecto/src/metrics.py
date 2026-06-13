from __future__ import annotations

from typing import Any

import numpy as np


def compute_similarity_matrix(image_features: np.ndarray, text_features: np.ndarray) -> np.ndarray:
    return image_features @ text_features.T


def ranks_from_similarity(sim: np.ndarray) -> np.ndarray:
    """Backward-compatible one-positive ranking: correct pair at the same index."""
    ranks = []
    for i in range(sim.shape[0]):
        order = np.argsort(-sim[i])
        rank = int(np.where(order == i)[0][0]) + 1
        ranks.append(rank)
    return np.array(ranks)


def ranks_from_matching_ids(sim: np.ndarray, query_ids: list[Any] | np.ndarray, candidate_ids: list[Any] | np.ndarray) -> np.ndarray:
    """Rank the first candidate whose id matches the query id.

    This supports Flickr-style evaluation where each image may have several
    valid captions. For image->text, query_ids are image ids and candidate_ids
    are the image ids associated with each caption. For text->image, use sim.T.
    """
    query_ids = np.asarray([str(x) for x in query_ids])
    candidate_ids = np.asarray([str(x) for x in candidate_ids])

    if sim.shape[0] != len(query_ids):
        raise ValueError(f"sim rows ({sim.shape[0]}) != query_ids ({len(query_ids)})")
    if sim.shape[1] != len(candidate_ids):
        raise ValueError(f"sim cols ({sim.shape[1]}) != candidate_ids ({len(candidate_ids)})")

    ranks = []
    for i, qid in enumerate(query_ids):
        positives = np.flatnonzero(candidate_ids == qid)
        if len(positives) == 0:
            raise ValueError(f"No hay candidato positivo para query_id={qid!r}")
        order = np.argsort(-sim[i])
        positive_ranks = np.flatnonzero(np.isin(order, positives)) + 1
        ranks.append(int(positive_ranks.min()))
    return np.array(ranks)


def summarize_ranks(ranks: np.ndarray) -> dict[str, float | list[int]]:
    n_candidates = len(ranks)
    return {
        "R@1": float(np.mean(ranks <= 1)),
        "R@5": float(np.mean(ranks <= min(5, n_candidates))),
        "R@10": float(np.mean(ranks <= min(10, n_candidates))),
        "MRR": float(np.mean(1.0 / ranks)),
        "MeanRank": float(np.mean(ranks)),
        "MedianRank": float(np.median(ranks)),
        "Ranks": ranks.astype(int).tolist(),
    }


def summarize_ranking(sim: np.ndarray) -> dict[str, float | list[int]]:
    return summarize_ranks(ranks_from_similarity(sim))


def summarize_ranking_by_id(
    sim: np.ndarray,
    query_ids: list[Any] | np.ndarray,
    candidate_ids: list[Any] | np.ndarray,
) -> dict[str, float | list[int]]:
    return summarize_ranks(ranks_from_matching_ids(sim, query_ids, candidate_ids))
