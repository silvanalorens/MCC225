from __future__ import annotations
import json
from pathlib import Path
from typing import Dict, List, Tuple
import pandas as pd

def load_metadata(csv_path: str | Path, root: str | Path | None = None) -> pd.DataFrame:
    csv_path = Path(csv_path)
    if root is None:
        root = Path('.')
    root = Path(root)
    df = pd.read_csv(csv_path)
    if 'filepath' not in df.columns:
        raise ValueError("metadata CSV must include a 'filepath' column")
    df['filepath'] = df['filepath'].astype(str).apply(lambda p: str((root / p).resolve()) if not Path(p).is_absolute() else p)
    if 'caption' not in df.columns:
        raise ValueError("metadata CSV must include a 'caption' column")
    if 'all_captions_json' in df.columns:
        df['all_captions'] = df['all_captions_json'].apply(lambda x: json.loads(x) if isinstance(x, str) and x else [])
    else:
        df['all_captions'] = df['caption'].apply(lambda x: [x])
    return df

def explode_all_captions(df: pd.DataFrame) -> pd.DataFrame:
    rows: List[Dict[str, str]] = []
    for image_idx, (_, row) in enumerate(df.iterrows()):
        captions = row.get('all_captions', None) or [row['caption']]
        for cap_idx, cap in enumerate(captions):
            rows.append({
                'image_index': image_idx,
                'image_id': row.get('image_id', f'img_{image_idx:04d}'),
                'filepath': row['filepath'],
                'caption_id': f"{row.get('image_id', f'img_{image_idx:04d}')}_{cap_idx}",
                'caption': cap,
                'label': row.get('label', ''),
            })
    return pd.DataFrame(rows)

def build_caption_targets(df: pd.DataFrame) -> Tuple[pd.DataFrame, Dict[int, List[int]], Dict[int, int]]:
    caption_df = explode_all_captions(df)
    image_to_text: Dict[int, List[int]] = {}
    text_to_image: Dict[int, int] = {}
    for text_idx, (_, row) in enumerate(caption_df.iterrows()):
        img_idx = int(row['image_index'])
        image_to_text.setdefault(img_idx, []).append(text_idx)
        text_to_image[text_idx] = img_idx
    return caption_df, image_to_text, text_to_image
