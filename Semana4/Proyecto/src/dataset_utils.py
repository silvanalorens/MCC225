from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import pandas as pd


def parse_captions(value: Any) -> list[str]:
    """Return a clean list of captions from JSON, list, tuple or scalar text."""
    if isinstance(value, list):
        return [str(x).strip() for x in value if str(x).strip()]
    if isinstance(value, tuple):
        return [str(x).strip() for x in value if str(x).strip()]
    if isinstance(value, str):
        value = value.strip()
        if not value:
            return []
        if value.startswith("["):
            try:
                decoded = json.loads(value)
                if isinstance(decoded, list):
                    return [str(x).strip() for x in decoded if str(x).strip()]
            except json.JSONDecodeError:
                pass
        return [value]
    if value is None:
        return []
    return [str(value).strip()]


def _resolve_filepath(path_value: str, root: Path) -> str:
    path = Path(path_value)
    if path.is_absolute():
        return str(path)
    return str((root / path).resolve())


def load_metadata(csv_path: str | Path, root: str | Path | None = None) -> pd.DataFrame:
    csv_path = Path(csv_path)
    if root is None:
        root = csv_path.parent.parent if csv_path.parent.name else Path(".")
    root = Path(root)

    df = pd.read_csv(csv_path)
    if "filepath" not in df.columns:
        raise ValueError("metadata CSV debe incluir una columna 'filepath'")
    if "caption" not in df.columns:
        raise ValueError("metadata CSV debe incluir una columna 'caption'")
    if "image_id" not in df.columns:
        df["image_id"] = [f"img_{i:06d}" for i in range(len(df))]
    if "label" not in df.columns:
        df["label"] = ""

    df["filepath"] = df["filepath"].astype(str).apply(lambda p: _resolve_filepath(p, root))
    df["caption"] = df["caption"].astype(str)
    df["image_id"] = df["image_id"].astype(str)

    if "all_captions_json" in df.columns:
        df["all_captions"] = df["all_captions_json"].apply(parse_captions)
    else:
        df["all_captions"] = df["caption"].apply(lambda x: [str(x)])

    df["all_captions"] = df.apply(
        lambda row: row["all_captions"] if row["all_captions"] else [row["caption"]],
        axis=1,
    )
    return df


def explode_all_captions(df: pd.DataFrame) -> pd.DataFrame:
    """Create one text row per caption, preserving the image_id for multi-positive retrieval."""
    rows: list[dict[str, Any]] = []
    for _, row in df.iterrows():
        image_id = str(row.get("image_id", ""))
        captions = row.get("all_captions", None) or [row["caption"]]
        for idx, caption in enumerate(captions):
            rows.append({
                "image_id": image_id,
                "filepath": row["filepath"],
                "caption_id": f"{image_id}_cap{idx:02d}",
                "caption": str(caption),
                "label": row.get("label", ""),
            })
    return pd.DataFrame(rows)


def first_caption_metadata(df: pd.DataFrame) -> pd.DataFrame:
    rows = []
    for _, row in df.iterrows():
        image_id = str(row.get("image_id", ""))
        rows.append({
            "image_id": image_id,
            "filepath": row["filepath"],
            "caption_id": f"{image_id}_cap00",
            "caption": str(row["caption"]),
            "label": row.get("label", ""),
        })
    return pd.DataFrame(rows)
