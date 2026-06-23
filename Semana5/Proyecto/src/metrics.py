from __future__ import annotations
from typing import Dict, Iterable, List
import numpy as np
import pandas as pd

def compute_similarity_matrix(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    return a @ b.T

def _best_positive_rank(scores: np.ndarray, positive_indices: Iterable[int]) -> int:
    order = np.argsort(-scores)
    pos_set = set(int(x) for x in positive_indices)
    for rank, idx in enumerate(order, start=1):
        if int(idx) in pos_set:
            return rank
    return len(order) + 1

def summarize_multi_target_ranking(sim: np.ndarray, positive_map: Dict[int, List[int]]) -> Dict[str, float | List[int]]:
    ranks: List[int] = []
    for query_idx in range(sim.shape[0]):
        pos = positive_map[query_idx]
        ranks.append(_best_positive_rank(sim[query_idx], pos))
    ranks_arr = np.asarray(ranks, dtype=np.int32)
    return {
        'R@1': float(np.mean(ranks_arr <= 1)),
        'R@5': float(np.mean(ranks_arr <= np.minimum(5, sim.shape[1]))),
        'R@10': float(np.mean(ranks_arr <= np.minimum(10, sim.shape[1]))),
        'MRR': float(np.mean(1.0 / ranks_arr)),
        'MeanRank': float(np.mean(ranks_arr)),
        'MedianRank': float(np.median(ranks_arr)),
        'Ranks': ranks_arr.tolist(),
    }

def per_query_ranks(sim: np.ndarray, positive_map: Dict[int, List[int]], query_ids: List[str]) -> pd.DataFrame:
    rows = []
    for query_idx in range(sim.shape[0]):
        rank = _best_positive_rank(sim[query_idx], positive_map[query_idx])
        rows.append({'query_index': query_idx, 'query_id': query_ids[query_idx], 'rank': int(rank)})
    return pd.DataFrame(rows)

def confusion_from_predictions(true_labels: List[str], pred_labels: List[str]) -> pd.DataFrame:
    labels = sorted(set(true_labels) | set(pred_labels))
    mat = pd.DataFrame(0, index=labels, columns=labels)
    for t, p in zip(true_labels, pred_labels):
        mat.loc[t, p] += 1
    return mat
