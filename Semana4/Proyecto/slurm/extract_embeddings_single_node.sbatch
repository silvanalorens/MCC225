#!/bin/bash -x
#SBATCH --job-name=mcc225_embed_extract
#SBATCH --nodes=1
#SBATCH --gres=gpu:1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=4
#SBATCH --mem=24G
#SBATCH --time=01:00:00
#SBATCH --output=outputs/logs/extract_%j.out

cd "${SLURM_SUBMIT_DIR}"

python scripts/02_build_embeddings.py \
  --metadata-csv data/bootstrap_flickr30k/metadata.csv \
  --model-name ViT-B-32 \
  --pretrained laion2b_s34b_b79k \
  --batch-size 16 \
  --caption-mode all \
  --output outputs/embeddings/bootstrap_embeddings.npz