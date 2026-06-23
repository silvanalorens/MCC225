#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "${SCRIPT_DIR}/.." && pwd)"
cd "${PROJECT_ROOT}"
export PYTHONPATH="${PROJECT_ROOT}:${PYTHONPATH:-}"

python scripts/00_verify_env.py
python scripts/02_build_embeddings.py \
  --metadata-csv data/bootstrap_flickr30k/metadata.csv \
  --model-name ViT-B-32 \
  --pretrained laion2b_s34b_b79k \
  --output outputs/embeddings/bootstrap_embeddings.npz
python scripts/03_eval_retrieval_metrics.py \
  --embeddings outputs/embeddings/bootstrap_embeddings.npz \
  --metadata-csv data/bootstrap_flickr30k/metadata.csv
python scripts/04_eval_zeroshot_prompt_ensembles.py \
  --embeddings outputs/embeddings/bootstrap_embeddings.npz \
  --metadata-csv data/bootstrap_flickr30k/metadata.csv \
  --prompt-config data/bootstrap_flickr30k/prompt_config.json
python scripts/05_compare_checkpoints.py \
  --metadata-csv data/bootstrap_flickr30k/metadata.csv \
  --checkpoint-config configs/checkpoints.yaml \
  --prompt-config data/bootstrap_flickr30k/prompt_config.json
python scripts/06_build_faiss_index.py \
  --embeddings outputs/embeddings/bootstrap_embeddings.npz \
  --metadata-csv data/bootstrap_flickr30k/metadata.csv \
  --queries-csv data/bootstrap_flickr30k/queries.csv
