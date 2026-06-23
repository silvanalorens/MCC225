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
  "${IMAGE}" \
  bash -lc 'pip install -r requirements-extra.txt && source scripts/activate_project_env.sh && bash scripts/run_local_pipeline.sh'
