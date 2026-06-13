#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")/.."

torchrun \
  --nproc_per_node=1 \
  -m open_clip_train.main \
  --dataset-type csv \
  --train-data data/bootstrap_flickr30k/metadata.csv \
  --val-data data/bootstrap_flickr30k/metadata.csv \
  --csv-img-key filepath \
  --csv-caption-key caption \
  --model ViT-B-32 \
  --pretrained laion2b_s34b_b79k \
  --batch-size 8 \
  --workers 2 \
  --precision amp \
  --epochs 1 \
  --lr 1e-5 \
  --wd 0.1 \
  --warmup 10 \
  --local-loss \
  --gather-with-grad \
  --logs outputs/logs/openclip_train_torchrun \
  --name week4_bootstrap_torchrun