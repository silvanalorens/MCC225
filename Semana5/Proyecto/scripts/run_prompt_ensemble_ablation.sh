#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."
export PYTHONPATH="${PWD}:${PYTHONPATH:-}"
python scripts/04_eval_zeroshot_prompt_ensembles.py   --embeddings outputs/embeddings/bootstrap_embeddings.npz   --metadata-csv data/bootstrap_flickr30k/metadata.csv   --prompt-config configs/prompt_ensemble.yaml   --output-summary outputs/metrics/zeroshot_prompt_summary_ensemble.yaml.csv   --output-predictions outputs/metrics/zeroshot_predictions_ensemble.yaml.csv   --output-confusion outputs/metrics/zeroshot_confusion_ensemble.yaml.csv
