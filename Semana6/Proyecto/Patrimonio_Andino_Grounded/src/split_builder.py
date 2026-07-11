from __future__ import annotations

import random
from collections import defaultdict
from typing import Any, Dict, Iterable, List, Tuple


def group_by_canonical_id(records: Iterable[Dict[str, Any]]) -> Dict[str, List[Dict[str, Any]]]:
    groups: Dict[str, List[Dict[str, Any]]] = defaultdict(list)
    for record in records:
        groups[record["canonical_id"]].append(record)
    return groups


def build_group_splits(
    records: List[Dict[str, Any]],
    train_ratio: float = 0.70,
    dev_ratio: float = 0.15,
    seed: int = 42,
) -> Dict[str, List[Dict[str, Any]]]:
    groups = list(group_by_canonical_id(records).items())
    rng = random.Random(seed)
    rng.shuffle(groups)

    n = len(groups)
    n_train = max(1, round(n * train_ratio))
    n_dev = max(1, round(n * dev_ratio)) if n >= 3 else 0

    train_groups = groups[:n_train]
    dev_groups = groups[n_train:n_train + n_dev]
    test_groups = groups[n_train + n_dev:]

    def flatten(items: List[Tuple[str, List[Dict[str, Any]]]], split_name: str) -> List[Dict[str, Any]]:
        out: List[Dict[str, Any]] = []
        for _, recs in items:
            for rec in recs:
                rec = dict(rec)
                rec["split"] = split_name
                out.append(rec)
        return out

    return {
        "train": flatten(train_groups, "train"),
        "dev": flatten(dev_groups, "dev"),
        "test": flatten(test_groups, "test"),
    }
