from __future__ import annotations

from typing import Iterable, List

from sklearn.feature_extraction.text import TfidfVectorizer


def build_text_corpus(records: Iterable[dict]) -> List[str]:
    texts: List[str] = []
    for record in records:
        xs = record.get("x_s", {})
        xt = record.get("x_t", {})
        xc = record.get("x_c", {})
        parts = [
            record.get("title") or "",
            record.get("description") or "",
            record.get("object_type") or "",
            record.get("culture") or "",
            record.get("provenance") or "",
            " ".join(record.get("tags", [])),
            xt.get("description", ""),
            " ".join(xt.get("keywords", [])),
            str(xs.get("pattern_type", "")),
            str(xs.get("material", "")),
            str(xs.get("analysis_type", "")),
            str(xc.get("chronology", "")),
            str(xc.get("museum", "")),
        ]
        texts.append(" ".join([p for p in parts if p]))
    return texts


def fit_tfidf(records: List[dict], ngram_range=(1, 2), min_df: int = 1):
    texts = build_text_corpus(records)
    vectorizer = TfidfVectorizer(lowercase=True, ngram_range=ngram_range, min_df=min_df)
    matrix = vectorizer.fit_transform(texts)
    return vectorizer, matrix
