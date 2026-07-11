#!/usr/bin/env bash
set -euo pipefail

PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "${PROJECT_ROOT}"

docker compose run --rm \
  -e BATCH_SIZE="${BATCH_SIZE:-16}" \
  -e EPOCHS="${EPOCHS:-1}" \
  -e WORKERS="${WORKERS:-4}" \
  -e PRECISION="${PRECISION:-amp}" \
  openclip \
  bash -lc 'pip install -r requirements-extra.txt && source scripts/activate_project_env.sh && bash scripts/90_openclip_finetune_csv_single_gpu.sh'
