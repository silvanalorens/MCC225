from __future__ import annotations
from typing import List
import numpy as np
from PIL import Image
import torch
import open_clip

def get_device() -> torch.device:
    return torch.device('cuda' if torch.cuda.is_available() else 'cpu')

def create_model(model_name: str, pretrained: str, device: torch.device | None = None):
    device = device or get_device()
    model, _, preprocess = open_clip.create_model_and_transforms(model_name, pretrained=pretrained)
    tokenizer = open_clip.get_tokenizer(model_name)
    model = model.to(device)
    model.eval()
    return model, preprocess, tokenizer, device

def _autocast_ctx(device: torch.device):
    return torch.autocast('cuda') if device.type == 'cuda' else torch.cpu.amp.autocast(enabled=False)

def encode_image_paths(model, preprocess, image_paths: List[str], device: torch.device, batch_size: int = 16) -> np.ndarray:
    feats = []
    with torch.no_grad():
        for start in range(0, len(image_paths), batch_size):
            batch_paths = image_paths[start:start+batch_size]
            images = [preprocess(Image.open(p).convert('RGB')) for p in batch_paths]
            tensor = torch.stack(images).to(device)
            with _autocast_ctx(device):
                f = model.encode_image(tensor)
            f = f / f.norm(dim=-1, keepdim=True)
            feats.append(f.detach().cpu().numpy().astype('float32'))
    return np.concatenate(feats, axis=0)

def encode_texts(model, tokenizer, texts: List[str], device: torch.device, batch_size: int = 64) -> np.ndarray:
    feats = []
    with torch.no_grad():
        for start in range(0, len(texts), batch_size):
            batch = texts[start:start+batch_size]
            tokens = tokenizer(batch).to(device)
            with _autocast_ctx(device):
                f = model.encode_text(tokens)
            f = f / f.norm(dim=-1, keepdim=True)
            feats.append(f.detach().cpu().numpy().astype('float32'))
    return np.concatenate(feats, axis=0)
