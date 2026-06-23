#!/bin/bash
#SBATCH --job-name=week5_train_single
#SBATCH --partition=gpu
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --gpus-per-node=1
#SBATCH --cpus-per-task=8
#SBATCH --mem=48G
#SBATCH --time=02:00:00
#SBATCH --output=outputs/logs/%x_%j.out

cd $SLURM_SUBMIT_DIR
python -m open_clip_train.main   --dataset-type csv   --train-data data/bootstrap_flickr30k/metadata.csv   --csv-separator ,   --csv-img-key filepath   --csv-caption-key caption   --model ViT-B-32   --pretrained laion2b_s34b_b79k   --batch-size 16   --epochs 1   --workers 4   --precision amp   --logs outputs/logs/fine_tune_slurm_single   --name week5_csv_slurm_single   --local-loss   --gather-with-grad
