from __future__ import annotations
from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))
import argparse, json
from pathlib import Path
import numpy as np
import pandas as pd
import yaml

from src.dataset_utils import load_metadata
from src.openclip_utils import create_model, encode_texts
from src.zeroshot import evaluate_prompt_templates, load_prompt_json
from src.io_utils import ensure_dir


def main():
    p = argparse.ArgumentParser()
    p.add_argument('--embeddings', required=True)
    p.add_argument('--metadata-csv', required=True)
    p.add_argument('--prompt-config', required=True)
    p.add_argument('--output-summary', default='outputs/metrics/zeroshot_prompt_summary.csv')
    p.add_argument('--output-predictions', default='outputs/metrics/zeroshot_predictions.csv')
    p.add_argument('--output-confusion', default='outputs/metrics/zeroshot_confusion.csv')
    args = p.parse_args()

    df = load_metadata(args.metadata_csv, root=Path('.'))
    if 'label' not in df.columns or df['label'].fillna('').eq('').all():
        raise ValueError('metadata must contain non-empty label column for zero-shot evaluation')

    if args.prompt_config.endswith('.json'):
        with open(args.prompt_config, 'r', encoding='utf-8') as f:
            cfg = json.load(f)
    else:
        with open(args.prompt_config, 'r', encoding='utf-8') as f:
            cfg = yaml.safe_load(f)

    bundle = np.load(args.embeddings, allow_pickle=True)
    image_features = bundle['image_features']
    model_name = str(bundle['model_name'])
    pretrained = str(bundle['pretrained'])

    model, _, tokenizer, device = create_model(model_name, pretrained)
    encoder_fn = lambda texts: encode_texts(model, tokenizer, texts, device)

    summary, pred_df, conf = evaluate_prompt_templates(
        image_features=image_features,
        true_labels=df['label'].astype(str).tolist(),
        label_map=cfg['label_map'],
        templates=cfg['templates'],
        encoder_fn=encoder_fn,
    )
    preds = df[['image_id', 'filepath', 'caption', 'label']].copy()
    preds['pred_label'] = pred_df['pred_label']
    preds['is_correct'] = preds['label'] == preds['pred_label']

    for out_path, obj in [
        (Path(args.output_summary), summary),
        (Path(args.output_predictions), preds),
        (Path(args.output_confusion), conf),
    ]:
        ensure_dir(out_path.parent)
        obj.to_csv(out_path, index=(out_path.suffix.lower() != '.csv' and False) or False)

    summary.to_csv(args.output_summary, index=False)
    preds.to_csv(args.output_predictions, index=False)
    conf.to_csv(args.output_confusion)
    print(summary)

if __name__ == '__main__':
    main()
