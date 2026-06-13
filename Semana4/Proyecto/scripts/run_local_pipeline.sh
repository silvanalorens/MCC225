#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")/.."
export PYTHONPATH="$PWD${PYTHONPATH:+:$PYTHONPATH}"

python scripts/00_verify_env.py

python scripts/02_build_embeddings.py \
  --metadata-csv data/bootstrap_flickr30k/metadata.csv \
  --model-name ViT-B-32 \
  --pretrained laion2b_s34b_b79k \
  --batch-size 16 \
  --caption-mode all \
  --output outputs/embeddings/bootstrap_embeddings.npz

python scripts/03_eval_retrieval.py \
  --embeddings outputs/embeddings/bootstrap_embeddings.npz \
  --metadata-csv data/bootstrap_flickr30k/metadata.csv \
  --output-json outputs/metrics/retrieval_metrics.json \
  --hard-negatives-csv outputs/metrics/hard_negatives.csv \
  --top-n-hard-negatives 8

python scripts/04_eval_zeroshot.py \
  --embeddings outputs/embeddings/bootstrap_embeddings.npz \
  --metadata-csv data/bootstrap_flickr30k/metadata.csv \
  --prompt-config data/bootstrap_flickr30k/prompt_config.json \
  --output-csv outputs/metrics/zeroshot_predictions.csv
