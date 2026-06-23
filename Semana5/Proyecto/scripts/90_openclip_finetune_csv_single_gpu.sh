#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "${SCRIPT_DIR}/.." && pwd)"
cd "${PROJECT_ROOT}"
export PYTHONPATH="${PROJECT_ROOT}:${PYTHONPATH:-}"
export CUDA_VISIBLE_DEVICES="${CUDA_VISIBLE_DEVICES:-0}"

MODEL="${MODEL:-ViT-B-32}"
PRETRAINED="${PRETRAINED:-laion2b_s34b_b79k}"
TRAIN_DATA="${TRAIN_DATA:-data/bootstrap_flickr30k/metadata.csv}"
CSV_SEPARATOR="${CSV_SEPARATOR:-,}"
BATCH_SIZE="${BATCH_SIZE:-16}"
EPOCHS="${EPOCHS:-1}"
WORKERS="${WORKERS:-4}"
PRECISION="${PRECISION:-amp}"
LR="${LR:-5e-6}"
WD="${WD:-0.1}"
LOGS="${LOGS:-outputs/logs/fine_tune_single_gpu}"
RUN_NAME="${RUN_NAME:-week5_csv_single_gpu}"

mkdir -p "${LOGS}"

echo "Fine-tuning OpenCLIP CSV single-GPU"
echo "PROJECT_ROOT=${PROJECT_ROOT}"
echo "MODEL=${MODEL}"
echo "PRETRAINED=${PRETRAINED}"
echo "TRAIN_DATA=${TRAIN_DATA}"
echo "CSV_SEPARATOR=${CSV_SEPARATOR}"
echo "BATCH_SIZE=${BATCH_SIZE}"
echo "EPOCHS=${EPOCHS}"
echo "WORKERS=${WORKERS}"
echo "PRECISION=${PRECISION}"
echo "CUDA_VISIBLE_DEVICES=${CUDA_VISIBLE_DEVICES}"

python - <<'PYDEP'
import importlib, sys
missing=[]
for mod in ["open_clip", "open_clip_train", "braceexpand", "webdataset"]:
    try:
        importlib.import_module(mod)
    except Exception as exc:
        missing.append(f"{mod}: {exc}")
if missing:
    print("Faltan dependencias para fine-tuning:")
    print("\n".join(missing))
    print("Ejecuta: pip install -r requirements-extra.txt")
    sys.exit(1)

import torch
print("torch.cuda.is_available() =", torch.cuda.is_available())
print("torch.cuda.device_count() =", torch.cuda.device_count())
if torch.cuda.is_available():
    print("GPU =", torch.cuda.get_device_name(0))
PYDEP

python -m open_clip_train.main \
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
  --lr "${LR}" \
  --wd "${WD}" \
  --logs "${LOGS}" \
  --name "${RUN_NAME}"
