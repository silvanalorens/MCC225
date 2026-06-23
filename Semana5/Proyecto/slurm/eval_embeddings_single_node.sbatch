#!/bin/bash
#SBATCH --job-name=week5_eval_single
#SBATCH --partition=gpu
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --gpus-per-node=1
#SBATCH --cpus-per-task=8
#SBATCH --mem=48G
#SBATCH --time=02:00:00
#SBATCH --output=outputs/logs/%x_%j.out

cd $SLURM_SUBMIT_DIR
export PYTHONPATH="${PWD}:${PYTHONPATH:-}"
python scripts/02_build_embeddings.py   --metadata-csv data/bootstrap_flickr30k/metadata.csv   --model-name ViT-B-32   --pretrained laion2b_s34b_b79k   --output outputs/embeddings/bootstrap_embeddings.npz
python scripts/03_eval_retrieval_metrics.py   --embeddings outputs/embeddings/bootstrap_embeddings.npz   --metadata-csv data/bootstrap_flickr30k/metadata.csv
