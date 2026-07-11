from __future__ import annotations

from typing import Dict, List

import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

from src.embedding_text import build_text_corpus, fit_tfidf


def fit_text_retriever(records: List[dict]) -> Dict[str, object]:
    vectorizer, matrix = fit_tfidf(records)
    return {
        "vectorizer": vectorizer,
        "matrix": matrix,
        "records": records,
        "texts": build_text_corpus(records),
    }


def retrieve_neighbors_tfidf(query: str, retriever: Dict[str, object], top_k: int = 3) -> List[dict]:
    query_vec = retriever["vectorizer"].transform([query])
    sims = cosine_similarity(query_vec, retriever["matrix"]).ravel()
    order = np.argsort(-sims)[:top_k]
    out: List[dict] = []
    for idx in order:
        record = retriever["records"][idx]
        out.append({
            "record_id": record["record_id"],
            "canonical_id": record["canonical_id"],
            "title": record["title"],
            "source": record["source"],
            "score": float(sims[idx]),
            "description": record["description"],
        })
    return out


def record_to_query(record: dict) -> str:
    fields = [
        record.get("title", ""),
        record.get("description", ""),
        record.get("object_type", ""),
        record.get("culture", ""),
        record.get("provenance", ""),
        " ".join(record.get("tags", [])),
    ]
    return " ".join([x for x in fields if x])
