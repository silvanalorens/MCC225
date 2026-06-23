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
            'rank': rank,
            'image_id': row.get('image_id', idx),
            'filepath': row['filepath'],
            'label': row.get('label', ''),
            'caption': row['caption'],
            'score': float(scores[idx]),
        })
    return pd.DataFrame(rows)

def topk_image_to_text(image_index: int, sim: np.ndarray, caption_df: pd.DataFrame, k: int = 5) -> pd.DataFrame:
    scores = sim[image_index]
    order = np.argsort(-scores)[:k]
    rows = []
    for rank, idx in enumerate(order, start=1):
        row = caption_df.iloc[idx]
        rows.append({
            'rank': rank,
            'image_id': row['image_id'],
            'caption_id': row['caption_id'],
            'caption': row['caption'],
            'label': row.get('label', ''),
            'score': float(scores[idx]),
        })
    return pd.DataFrame(rows)

def mine_hard_negatives(sim: np.ndarray, caption_df: pd.DataFrame, top_n: int = 15) -> pd.DataFrame:
    rows = []
    for image_index in range(sim.shape[0]):
        order = np.argsort(-sim[image_index])
        for idx in order:
            cap_row = caption_df.iloc[idx]
            if int(cap_row['image_index']) == image_index:
                continue
            rows.append({
                'image_index': image_index,
                'image_id': caption_df[caption_df['image_index'] == image_index].iloc[0]['image_id'],
                'negative_caption_id': cap_row['caption_id'],
                'negative_caption': cap_row['caption'],
                'negative_label': cap_row.get('label', ''),
                'score': float(sim[image_index, idx]),
            })
            break
    df = pd.DataFrame(rows).sort_values('score', ascending=False).head(top_n)
    return df.reset_index(drop=True)
