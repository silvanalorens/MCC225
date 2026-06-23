#!/usr/bin/env bash
set -euo pipefail

PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
IMAGE="${MCC225_IMAGE:-mcc225_gpu:latest}"

cd "${PROJECT_ROOT}"

docker run --rm --gpus all \
  -v "${PROJECT_ROOT}:/workspace/Proyecto" \
  -w /workspace/Proyecto \
  -e PYTHONPATH=/workspace/Proyecto \
  -e CUDA_VISIBLE_DEVICES="${CUDA_VISIBLE_DEVICES:-0}" \
  -e BATCH_SIZE="${BATCH_SIZE:-16}" \
  -e EPOCHS="${EPOCHS:-1}" \
  -e WORKERS="${WORKERS:-4}" \
  -e PRECISION="${PRECISION:-amp}" \
  -e MODEL="${MODEL:-ViT-B-32}" \
  -e PRETRAINED="${PRETRAINED:-laion2b_s34b_b79k}" \
  "${IMAGE}" \
  bash -lc 'pip install -r requirements-extra.txt && source scripts/activate_project_env.sh && bash scripts/90_openclip_finetune_csv_single_gpu.sh'
