#!/usr/bin/env bash
set -euo pipefail

PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "${PROJECT_ROOT}"

docker compose run --rm openclip \
  bash -lc 'pip install -r requirements-extra.txt && source scripts/activate_project_env.sh && bash scripts/run_local_pipeline.sh'
