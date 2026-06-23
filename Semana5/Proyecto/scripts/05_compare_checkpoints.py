from __future__ import annotations
from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))
import argparse
from pathlib import Path
import numpy as np
import pandas as pd
import yaml

from src.dataset_utils import load_metadata, build_caption_targets
from src.metrics import compute_similarity_matrix, summarize_multi_target_ranking
from src.openclip_utils import create_model, encode_image_paths, encode_texts
from src.zeroshot import evaluate_prompt_templates
from src.io_utils import ensure_dir


def main():
    p = argparse.ArgumentParser()
    p.add_argument('--metadata-csv', required=True)
    p.add_argument('--checkpoint-config', required=True)
    p.add_argument('--prompt-config', required=True)
    p.add_argument('--output-csv', default='outputs/metrics/checkpoint_comparison.csv')
    args = p.parse_args()

    df = load_metadata(args.metadata_csv, root=Path('.'))
    caption_df, image_to_text, text_to_image = build_caption_targets(df)
    text_positive = {idx: [img_idx] for idx, img_idx in text_to_image.items()}
    with open(args.checkpoint_config, 'r', encoding='utf-8') as f:
        ckpts = yaml.safe_load(f)['checkpoints']
    with open(args.prompt_config, 'r', encoding='utf-8') as f:
        if args.prompt_config.endswith('.json'):
            import json
            prompt_cfg = json.load(f)
        else:
            prompt_cfg = yaml.safe_load(f)

    rows = []
    for ckpt in ckpts:
        try:
            model, preprocess, tokenizer, device = create_model(ckpt['model_name'], ckpt['pretrained'])
            img_feats = encode_image_paths(model, preprocess, df['filepath'].tolist(), device, batch_size=8)
            txt_feats = encode_texts(model, tokenizer, caption_df['caption'].tolist(), device, batch_size=32)
            sim = compute_similarity_matrix(img_feats, txt_feats)
            i2t = summarize_multi_target_ranking(sim, image_to_text)
            t2i = summarize_multi_target_ranking(sim.T, text_positive)
            encoder_fn = lambda texts: encode_texts(model, tokenizer, texts, device)
            summary, _, _ = evaluate_prompt_templates(img_feats, df['label'].astype(str).tolist(), prompt_cfg['label_map'], prompt_cfg['templates'], encoder_fn)
            ensemble_acc = float(summary[summary['mode'] == 'prompt_ensemble']['accuracy'].iloc[0])
            rows.append({
                'tag': ckpt.get('tag', ckpt['model_name']),
                'model_name': ckpt['model_name'],
                'pretrained': ckpt['pretrained'],
                'i2t_R@1': i2t['R@1'],
                'i2t_MRR': i2t['MRR'],
                't2i_R@1': t2i['R@1'],
                't2i_MRR': t2i['MRR'],
                'zeroshot_ensemble_acc': ensemble_acc,
                'status': 'ok',
            })
        except Exception as e:
            rows.append({
                'tag': ckpt.get('tag', ckpt['model_name']),
                'model_name': ckpt['model_name'],
                'pretrained': ckpt['pretrained'],
                'status': f'error: {e}',
            })
    out = Path(args.output_csv)
    ensure_dir(out.parent)
    pd.DataFrame(rows).to_csv(out, index=False)
    print('Saved', out)

if __name__ == '__main__':
    main()
