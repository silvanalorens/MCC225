#!/bin/bash -x
#SBATCH --job-name=mcc225_openclip_single
#SBATCH --nodes=1
#SBATCH --gres=gpu:1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=6
#SBATCH --mem=32G
#SBATCH --time=02:00:00
#SBATCH --output=outputs/logs/slurm_single_%j.out

cd "${SLURM_SUBMIT_DIR}"

python -m open_clip_train.main \
  --dataset-type csv \
  --train-data data/bootstrap_flickr30k/metadata.csv \
  --val-data data/bootstrap_flickr30k/metadata.csv \
  --csv-img-key filepath \
  --csv-caption-key caption \
  --model ViT-B-32 \
  --pretrained laion2b_s34b_b79k \
  --batch-size 8 \
  --workers 4 \
  --precision amp \
  --epochs 1 \
  --lr 1e-5 \
  --wd 0.1 \
  --warmup 10 \
  --logs outputs/logs/openclip_slurm_single \
  --name week4_slurm_single