#!/bin/bash
#SBATCH --job-name=week5_train_multi
#SBATCH --partition=gpu
#SBATCH --nodes=2
#SBATCH --ntasks-per-node=1
#SBATCH --gpus-per-node=4
#SBATCH --cpus-per-task=8
#SBATCH --mem=96G
#SBATCH --time=04:00:00
#SBATCH --output=outputs/logs/%x_%j.out

cd $SLURM_SUBMIT_DIR
export MASTER_ADDR=$(scontrol show hostnames "$SLURM_JOB_NODELIST" | head -n 1)
export MASTER_PORT=29500
export WORLD_SIZE=$((SLURM_NNODES * SLURM_GPUS_ON_NODE))

srun torchrun   --nnodes=$SLURM_NNODES   --nproc_per_node=$SLURM_GPUS_ON_NODE   --rdzv_backend=c10d   --rdzv_endpoint=$MASTER_ADDR:$MASTER_PORT   -m open_clip_train.main   --dataset-type webdataset   --train-data '/path/to/shards/{000000..000127}.tar'   --train-num-samples 128000   --batch-size 64   --workers 8   --precision amp   --model ViT-B-32   --logs outputs/logs/fine_tune_slurm_multi   --name week5_webdataset_multi   --local-loss   --gather-with-grad
