#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "${SCRIPT_DIR}/.." && pwd)"
cd "${PROJECT_ROOT}"
export PYTHONPATH="${PROJECT_ROOT}:${PYTHONPATH:-}"

CANDIDATES="${BATCH_CANDIDATES:-8 16 24 32}"
EPOCHS="${EPOCHS:-1}"
WORKERS="${WORKERS:-4}"
PRECISION="${PRECISION:-amp}"

mkdir -p outputs/logs/batch_sweep

echo "Barrido simple de batch size single-GPU"
echo "Candidatos: ${CANDIDATES}"

BEST=""
for bs in ${CANDIDATES}; do
  echo "--- Probando BATCH_SIZE=${bs} ---"
  if BATCH_SIZE="${bs}" EPOCHS="${EPOCHS}" WORKERS="${WORKERS}" PRECISION="${PRECISION}" \
    LOGS="outputs/logs/batch_sweep/bs_${bs}" RUN_NAME="week5_bs_${bs}" \
    bash scripts/90_openclip_finetune_csv_single_gpu.sh; then
    BEST="${bs}"
    echo "OK: BATCH_SIZE=${bs}"
  else
    echo "FALLÓ: BATCH_SIZE=${bs}"
    break
  fi
done

echo "Mejor batch size probado sin error: ${BEST:-ninguno}"
