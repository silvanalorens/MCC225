#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "${SCRIPT_DIR}/.." && pwd)"
cd "${PROJECT_ROOT}"
export PYTHONPATH="${PROJECT_ROOT}:${PYTHONPATH:-}"

# Referencia multi-GPU. No usar en una sola GPU.
# Para una GPU ejecuta scripts/91_openclip_finetune_csv_torchrun.sh.

NPROC_PER_NODE="${NPROC_PER_NODE:-2}"
MODEL="${MODEL:-ViT-B-32}"
PRETRAINED="${PRETRAINED:-laion2b_s34b_b79k}"
TRAIN_DATA="${TRAIN_DATA:-data/bootstrap_flickr30k/metadata.csv}"
CSV_SEPARATOR="${CSV_SEPARATOR:-,}"
BATCH_SIZE="${BATCH_SIZE:-8}"
EPOCHS="${EPOCHS:-1}"
WORKERS="${WORKERS:-4}"
PRECISION="${PRECISION:-amp}"
LOG_DIR="${LOG_DIR:-outputs/logs/fine_tune_torchrun_multi_gpu}"
RUN_NAME="${RUN_NAME:-week5_csv_torchrun_multi_gpu}"

mkdir -p "${LOG_DIR}"

torchrun \
  --standalone \
  --nnodes=1 \
  --nproc_per_node="${NPROC_PER_NODE}" \
  scripts/openclip_train_entrypoint.py \
  --dataset-type csv \
  --train-data "${TRAIN_DATA}" \
  --csv-separator "${CSV_SEPARATOR}" \
  --csv-img-key filepath \
  --csv-caption-key caption \
  --model "${MODEL}" \
  --pretrained "${PRETRAINED}" \
  --batch-size "${BATCH_SIZE}" \
  --epochs "${EPOCHS}" \
  --workers "${WORKERS}" \
  --precision "${PRECISION}" \
  --logs "${LOG_DIR}" \
  --name "${RUN_NAME}" \
  --local-loss \
  --gather-with-grad
