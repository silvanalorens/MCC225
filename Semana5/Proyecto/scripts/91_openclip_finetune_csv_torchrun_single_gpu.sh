#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "${SCRIPT_DIR}/.." && pwd)"
cd "${PROJECT_ROOT}"
export PYTHONPATH="${PROJECT_ROOT}:${PYTHONPATH:-}"
export CUDA_VISIBLE_DEVICES="${CUDA_VISIBLE_DEVICES:-0}"

# Versión segura para una sola GPU.
# Usa un archivo Python como training_script posicional de torchrun.
# El separador "--" fuerza a torchrun a dejar de parsear opciones,
# por lo que --logs y otros argumentos quedan del lado de OpenCLIP.

NPROC_PER_NODE="${NPROC_PER_NODE:-1}"
MODEL="${MODEL:-ViT-B-32}"
PRETRAINED="${PRETRAINED:-laion2b_s34b_b79k}"
TRAIN_DATA="${TRAIN_DATA:-data/bootstrap_flickr30k/metadata.csv}"
CSV_SEPARATOR="${CSV_SEPARATOR:-,}"
BATCH_SIZE="${BATCH_SIZE:-16}"
EPOCHS="${EPOCHS:-1}"
WORKERS="${WORKERS:-4}"
PRECISION="${PRECISION:-amp}"
LOG_DIR="${LOG_DIR:-outputs/logs/fine_tune_torchrun_single_gpu}"
RUN_NAME="${RUN_NAME:-week5_csv_torchrun_single_gpu}"

if [[ "${NPROC_PER_NODE}" != "1" ]]; then
  echo "Este script es para single-GPU. Usa NPROC_PER_NODE=1." >&2
  exit 2
fi

mkdir -p "${LOG_DIR}"

torchrun \
  --standalone \
  --nnodes=1 \
  --nproc_per_node="${NPROC_PER_NODE}" \
  -- \
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
  --name "${RUN_NAME}"
