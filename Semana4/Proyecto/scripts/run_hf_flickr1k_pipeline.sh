#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")/.."
export PYTHONPATH="$PWD${PYTHONPATH:+:$PYTHONPATH}"

python scripts/00_verify_env.py

python scripts/01_prepare_flickr30k_from_hf.py \
  --dataset-name Vishva007/Flickr-Dataset-1k \
  --hf-split train \
  --output-root data/processed/flickr1k_hf \
  --train-limit 512 \
  --val-limit 50 \
  --test-limit 50

python scripts/02_build_embeddings.py \
  --metadata-csv data/processed/flickr1k_hf/all.csv \
  --model-name ViT-B-32 \
  --pretrained laion2b_s34b_b79k \
  --batch-size 32 \
  --caption-mode all \
  --output outputs/embeddings/flickr1k_embeddings.npz

python scripts/03_eval_retrieval.py \
  --embeddings outputs/embeddings/flickr1k_embeddings.npz \
  --metadata-csv data/processed/flickr1k_hf/all.csv \
  --output-json outputs/metrics/flickr1k_retrieval_metrics.json \
  --hard-negatives-csv outputs/metrics/flickr1k_hard_negatives.csv \
  --top-n-hard-negatives 20
