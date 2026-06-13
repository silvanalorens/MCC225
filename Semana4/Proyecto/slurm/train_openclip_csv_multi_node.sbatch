#!/bin/bash -x
#SBATCH --job-name=mcc225_openclip_multi
#SBATCH --nodes=2
#SBATCH --gres=gpu:1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=6
#SBATCH --mem=32G
#SBATCH --time=02:00:00
#SBATCH --output=outputs/logs/slurm_multi_%j.out
#SBATCH --wait-all-nodes=1

cd "${SLURM_SUBMIT_DIR}"


export MASTER_PORT=12802
master_addr=$(scontrol show hostnames "$SLURM_JOB_NODELIST" | head -n 1)
export MASTER_ADDR="${master_addr}"

torchrun \
  --nnodes="${SLURM_JOB_NUM_NODES}" \
  --nproc_per_node=1 \
  --rdzv_backend=c10d \
  --rdzv_endpoint="${MASTER_ADDR}:${MASTER_PORT}" \
  -m open_clip_train.main \
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
  --local-loss \
  --gather-with-grad \
  --logs outputs/logs/openclip_slurm_multi \
  --name week4_slurm_multi