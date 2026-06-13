#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")/.."
export PYTHONPATH="$PWD${PYTHONPATH:+:$PYTHONPATH}"

torchrun --standalone --nnodes=1 --nproc_per_node=1 scripts/02_build_embeddings.py \
  --metadata-csv data/bootstrap_flickr30k/metadata.csv \
  --model-name ViT-B-32 \
  --pretrained laion2b_s34b_b79k \
  --batch-size 16 \
  --caption-mode all \
  --output outputs/embeddings/bootstrap_embeddings_torchrun.npz
