
from __future__ import annotations
from typing import Dict, List, Tuple
import numpy as np

def build_class_prompts(label_map: Dict[str, str], templates: List[str]) -> Tuple[List[str], List[str]]:
    internal_labels = list(label_map.keys())
    class_names = [label_map[k] for k in internal_labels]
    prompts = [templates[0].format(name) for name in class_names]
    return internal_labels, prompts

def predict(image_features: np.ndarray, prompt_features: np.ndarray, internal_labels: List[str]) -> List[str]:
    scores = image_features @ prompt_features.T
    pred_idx = scores.argmax(axis=1)
    return [internal_labels[i] for i in pred_idx]
