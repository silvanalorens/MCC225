from __future__ import annotations

from pathlib import Path
from typing import Optional

import numpy as np
from PIL import Image


def lightweight_image_embedding(image_path: str | Path) -> Optional[np.ndarray]:
    """
    Embeddings muy pequeñaos basadas en estadísticas RGB redimensionadas.

    Esto no sustituye a un codificador de visión real.
    """

    image_path = Path(image_path)
    if not image_path.exists():
        return None
    image = Image.open(image_path).convert("RGB").resize((32, 32))
    arr = np.asarray(image).astype("float32") / 255.0
    return arr.mean(axis=(0, 1))
