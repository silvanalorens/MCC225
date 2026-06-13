from __future__ import annotations

import numpy as np
import pandas as pd


def topk_text_to_image(query_feature: np.ndarray, image_features: np.ndarray, metadata: pd.DataFrame, k: int = 5) -> pd.DataFrame:
    scores = (query_feature @ image_features.T).squeeze()
    order = np.argsort(-scores)[:k]
    rows = []
    for rank, idx in enumerate(order, start=1):
        row = metadata.iloc[idx]
        rows.append({
            "rank": rank,
            "image_id": row.get("image_id", idx),
            "filepath": row["filepath"],
            "caption": row.get("caption", ""),
            "label": row.get("label", ""),
            "score": float(scores[idx]),
        })
    return pd.DataFrame(rows)


def topk_image_to_text(image_feature: np.ndarray, text_features: np.ndarray, text_metadata: pd.DataFrame, k: int = 5) -> pd.DataFrame:
    scores = (image_feature @ text_features.T).squeeze()
    order = np.argsort(-scores)[:k]
    rows = []
    for rank, idx in enumerate(order, start=1):
        row = text_metadata.iloc[idx]
        rows.append({
            "rank": rank,
            "image_id": row.get("image_id", idx),
            "caption_id": row.get("caption_id", ""),
            "caption": row["caption"],
            "label": row.get("label", ""),
            "score": float(scores[idx]),
        })
    return pd.DataFrame(rows)


def mine_hard_negatives(
    sim: np.ndarray,
    image_metadata: pd.DataFrame,
    text_metadata: pd.DataFrame | None = None,
    top_n: int = 10,
) -> pd.DataFrame:
    """Mine high-scoring mismatched image-caption pairs.

    Positive pairs are excluded by image_id, not by diagonal index. This matters
    when each image has multiple valid captions.
    """
    if text_metadata is None:
        text_metadata = image_metadata.copy()
        if "caption_id" not in text_metadata.columns:
            text_metadata["caption_id"] = [f"{row.get('image_id', i)}_cap00" for i, row in text_metadata.iterrows()]

    if sim.shape[0] != len(image_metadata):
        raise ValueError("sim rows must match image_metadata length")
    if sim.shape[1] != len(text_metadata):
        raise ValueError("sim columns must match text_metadata length")

    candidates = []
    for image_idx in range(sim.shape[0]):
        image_row = image_metadata.iloc[image_idx]
        image_id = str(image_row.get("image_id", image_idx))
        for text_idx in range(sim.shape[1]):
            text_row = text_metadata.iloc[text_idx]
            text_image_id = str(text_row.get("image_id", text_idx))
            if image_id == text_image_id:
                continue
            candidates.append({
                "image_index": image_idx,
                "text_index": text_idx,
                "score": float(sim[image_idx, text_idx]),
                "image_id": image_id,
                "text_image_id": text_image_id,
                "caption_id": text_row.get("caption_id", ""),
                "image_label": image_row.get("label", ""),
                "text_label": text_row.get("label", ""),
                "image_caption": image_row.get("caption", ""),
                "negative_caption": text_row["caption"],
                "image_filepath": image_row["filepath"],
            })

    if not candidates:
        return pd.DataFrame()
    return pd.DataFrame(candidates).sort_values("score", ascending=False).head(top_n).reset_index(drop=True)
