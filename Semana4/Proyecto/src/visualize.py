
from __future__ import annotations
from pathlib import Path
import matplotlib.pyplot as plt
from PIL import Image
import pandas as pd

def show_gallery(metadata: pd.DataFrame, ncols: int = 3, figsize=(12, 8)):
    n = len(metadata)
    nrows = (n + ncols - 1) // ncols
    fig, axes = plt.subplots(nrows, ncols, figsize=figsize)
    axes = axes.flatten() if hasattr(axes, "flatten") else [axes]
    for ax in axes[n:]:
        ax.axis("off")
    for ax, (_, row) in zip(axes, metadata.iterrows()):
        img = Image.open(row["filepath"]).convert("RGB")
        ax.imshow(img)
        ax.set_title(f'{row.get("image_id","")}\n{row.get("label","")}', fontsize=9)
        ax.axis("off")
    plt.tight_layout()
    return fig

def show_retrieval_results(results: pd.DataFrame, figsize=(12, 4)):
    fig, axes = plt.subplots(1, len(results), figsize=figsize)
    if len(results) == 1:
        axes = [axes]
    for ax, (_, row) in zip(axes, results.iterrows()):
        img = Image.open(row["filepath"]).convert("RGB")
        ax.imshow(img)
        ax.set_title(f'#{row["rank"]}\n{row["label"]}\n{row["score"]:.3f}', fontsize=9)
        ax.axis("off")
    plt.tight_layout()
    return fig
