import json
import os
import random
import subprocess
import sys
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Sequence, Tuple

import numpy as np
import pandas as pd
import torch
from PIL import Image, ImageFilter, ImageOps
from tqdm.auto import tqdm

SEED = 22514
random.seed(SEED)
np.random.seed(SEED)
torch.manual_seed(SEED)

DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")

@dataclass
class ExperimentConfig:
    dataset_name: str = "jxie/flickr8k"
    dataset_split: str = "train"
    max_samples: int = 240
    evaluation_samples: int = 160
    caption_samples: int = 48
    error_cases: int = 40
    batch_size: int = 16
    clip_model_name: str = "openai/clip-vit-base-patch32"
    blip_model_name: str = "Salesforce/blip-image-captioning-base"
    use_blip_captioner: bool = False
    allow_demo_mode: bool = False
    repo_root: str = "."

CONFIG = ExperimentConfig()

ROOT = Path(CONFIG.repo_root).resolve()
DATA_RAW = ROOT / "data" / "raw"
DATA_PROCESSED = ROOT / "data" / "processed"
OUTPUT_FIGURES = ROOT / "outputs" / "figures"
OUTPUT_TABLES = ROOT / "outputs" / "tables"
OUTPUT_METRICS = ROOT / "outputs" / "metrics"
REPORTS = ROOT / "reports"

for folder in [DATA_RAW, DATA_PROCESSED, OUTPUT_FIGURES, OUTPUT_TABLES, OUTPUT_METRICS, REPORTS]:
    folder.mkdir(parents=True, exist_ok=True)

print(f"Dispositivo activo: {DEVICE}")
print(json.dumps(asdict(CONFIG), indent=2, ensure_ascii=False))