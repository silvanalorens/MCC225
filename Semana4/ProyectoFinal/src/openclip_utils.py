from __future__ import annotations

from contextlib import nullcontext
from pathlib import Path
from typing import List
import warnings

import numpy as np
from PIL import Image
import torch
import open_clip


def get_device() -> torch.device:
    """Return CUDA when available; otherwise CPU."""
    return torch.device("cuda" if torch.cuda.is_available() else "cpu")


def create_model(
    model_name: str,
    pretrained: str,
    device: torch.device | None = None,
    *,
    suppress_known_warnings: bool = True,
):
    """Create an OpenCLIP model and tokenizer for inference.

    The warning about ``torch.load(weights_only=False)`` is emitted inside
    OpenCLIP when it loads trusted pretrained checkpoints. We suppress only
    that known warning so that classroom logs remain readable; all other
    warnings are still shown.
    """
    device = device or get_device()

    with warnings.catch_warnings():
        if suppress_known_warnings:
            warnings.filterwarnings(
                "ignore",
                message=r"You are using `torch\.load` with `weights_only=False`.*",
                category=FutureWarning,
            )
        model, _, preprocess = open_clip.create_model_and_transforms(
            model_name,
            pretrained=pretrained,
        )

    tokenizer = open_clip.get_tokenizer(model_name)
    model = model.to(device)
    model.eval()
    return model, preprocess, tokenizer, device


def _autocast_ctx(device: torch.device):
    """Use modern AMP APIs and avoid deprecated torch.cpu.amp.autocast."""
    if device.type == "cuda":
        return torch.amp.autocast(device_type="cuda")
    return nullcontext()


def encode_image_paths(
    model,
    preprocess,
    image_paths: List[str],
    device: torch.device,
    batch_size: int = 32,
) -> np.ndarray:
    feats = []
    with torch.no_grad():
        for start in range(0, len(image_paths), batch_size):
            batch_paths = image_paths[start : start + batch_size]
            images = []
            for p in batch_paths:
                path = Path(p)
                if not path.exists():
                    raise FileNotFoundError(f"No existe la imagen: {path}")
                with Image.open(path) as img:
                    images.append(preprocess(img.convert("RGB")))
            tensor = torch.stack(images).to(device)
            with _autocast_ctx(device):
                f = model.encode_image(tensor)
            f = f / f.norm(dim=-1, keepdim=True)
            feats.append(f.detach().cpu().numpy().astype("float32"))
    if not feats:
        raise ValueError("No se recibieron rutas de imágenes para codificar.")
    return np.concatenate(feats, axis=0)


def encode_texts(
    model,
    tokenizer,
    texts: List[str],
    device: torch.device,
    batch_size: int = 64,
) -> np.ndarray:
    feats = []
    with torch.no_grad():
        for start in range(0, len(texts), batch_size):
            batch = [str(x) for x in texts[start : start + batch_size]]
            tokens = tokenizer(batch).to(device)
            with _autocast_ctx(device):
                f = model.encode_text(tokens)
            f = f / f.norm(dim=-1, keepdim=True)
            feats.append(f.detach().cpu().numpy().astype("float32"))
    if not feats:
        raise ValueError("No se recibieron textos para codificar.")
    return np.concatenate(feats, axis=0)
