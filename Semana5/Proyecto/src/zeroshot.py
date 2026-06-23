from __future__ import annotations
import json
from pathlib import Path
from typing import Dict, List, Tuple
import numpy as np
import pandas as pd
from .metrics import confusion_from_predictions

def load_prompt_json(path: str | Path) -> Dict:
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)

def build_prompt_bank(label_map: Dict[str, str], templates: List[str]) -> Tuple[List[str], Dict[str, List[str]]]:
    labels = list(label_map.keys())
    prompt_bank = {label: [template.format(label_map[label]) for template in templates] for label in labels}
    return labels, prompt_bank

def aggregate_label_embeddings(prompt_bank: Dict[str, List[str]], encoder_fn) -> Tuple[List[str], np.ndarray]:
    labels = list(prompt_bank.keys())
    label_vectors = []
    for label in labels:
        feats = encoder_fn(prompt_bank[label])
        vec = feats.mean(axis=0)
        vec = vec / np.linalg.norm(vec)
        label_vectors.append(vec.astype('float32'))
    return labels, np.stack(label_vectors)

def predict(image_features: np.ndarray, label_features: np.ndarray, labels: List[str]) -> Tuple[List[str], np.ndarray]:
    scores = image_features @ label_features.T
    pred_idx = scores.argmax(axis=1)
    preds = [labels[i] for i in pred_idx]
    return preds, scores

def evaluate_prompt_templates(image_features: np.ndarray, true_labels: List[str], label_map: Dict[str, str], templates: List[str], encoder_fn):
    rows = []
    all_preds = {}
    for template in templates:
        single_bank = {label: [template.format(label_map[label])] for label in label_map.keys()}
        labels, feats = aggregate_label_embeddings(single_bank, encoder_fn)
        preds, scores = predict(image_features, feats, labels)
        acc = float(np.mean([p == y for p, y in zip(preds, true_labels)]))
        rows.append({'mode': 'single_template', 'template': template, 'accuracy': acc})
        all_preds[template] = preds
    labels, ensemble_feats = aggregate_label_embeddings({label: [t.format(label_map[label]) for t in templates] for label in label_map.keys()}, encoder_fn)
    ensemble_preds, ensemble_scores = predict(image_features, ensemble_feats, labels)
    ensemble_acc = float(np.mean([p == y for p, y in zip(ensemble_preds, true_labels)]))
    rows.append({'mode': 'prompt_ensemble','template': '; '.join(templates),'accuracy': ensemble_acc})
    summary = pd.DataFrame(rows).sort_values(['accuracy', 'mode'], ascending=[False, True]).reset_index(drop=True)
    pred_df = pd.DataFrame({'true_label': true_labels, 'pred_label': ensemble_preds})
    conf = confusion_from_predictions(true_labels, ensemble_preds)
    return summary, pred_df, conf
