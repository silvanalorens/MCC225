#!/usr/bin/env bash
set -euo pipefail

PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
IMAGE="${MCC225_IMAGE:-mcc225_gpu:latest}"
CONTAINER_NAME="${MCC225_CONTAINER:-mcc225_openclip_shell}"

cd "${PROJECT_ROOT}"

docker run --rm -it --gpus all \
  --name "${CONTAINER_NAME}" \
  -v "${PROJECT_ROOT}:/workspace/Proyecto" \
  -w /workspace/Proyecto \
  -e PYTHONPATH=/workspace/Proyecto \
  -e CUDA_VISIBLE_DEVICES="${CUDA_VISIBLE_DEVICES:-0}" \
  "${IMAGE}" \
  bash
