# ============================================================
# 01_internvideo2_extract_embeddings.py
# Extracción de embeddings con InternVideo2 para MSR-VTT
# ============================================================

import os
import cv2
import numpy as np
import pandas as pd
import torch
from tqdm import tqdm
from transformers import AutoProcessor, AutoModel

# ============================================================
# CONFIGURACIÓN
# ============================================================

BASE_DIR = "/workspace/Semana4/ProyectoFinal"

CSV_PATH = f"{BASE_DIR}/data/msr-vtt/msrvtt_subset.csv"
VIDEO_DIR = f"{BASE_DIR}/data/msr-vtt/videos"

OUTPUT_DIR = f"{BASE_DIR}/outputs/internvideo2_embeddings"
os.makedirs(OUTPUT_DIR, exist_ok=True)

EMB_FILE = f"{OUTPUT_DIR}/embeddings.npy"
META_FILE = f"{OUTPUT_DIR}/metadata.csv"

MODEL_NAME = "OpenGVLab/InternVideo2-Stage1-1B-224p-K700"

DEVICE = "cpu"  # tu caso

NUM_FRAMES = 8

# ============================================================
# MODELO
# ============================================================

print("Cargando modelo InternVideo2...")

processor = AutoProcessor.from_pretrained(
    MODEL_NAME,
    trust_remote_code=True
)

model = AutoModel.from_pretrained(
    MODEL_NAME,
    trust_remote_code=True
).to(DEVICE)

model.eval()

print("Modelo cargado OK")

# ============================================================
# DATASET
# ============================================================

df = pd.read_csv(CSV_PATH)

print("Videos:", len(df))

# ============================================================
# FUNCIONES
# ============================================================

def sample_frames(video_path, num_frames=8):
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        return None

    total = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    if total <= 0:
        return None

    idxs = np.linspace(0, total - 1, num_frames).astype(int)

    frames = []

    for i in idxs:
        cap.set(cv2.CAP_PROP_POS_FRAMES, i)
        ret, frame = cap.read()

        if not ret:
            continue

        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frames.append(frame)

    cap.release()

    if len(frames) == 0:
        return None

    return frames


# ============================================================
# LOOP PRINCIPAL
# ============================================================

embeddings = []
metadata = []

for i in tqdm(range(len(df))):

    row = df.iloc[i]
    video_path = os.path.join(VIDEO_DIR, row["video_id"] + ".mp4")

    if not os.path.exists(video_path):
        continue

    frames = sample_frames(video_path, NUM_FRAMES)

    if frames is None:
        continue

    try:
        inputs = processor(images=frames, return_tensors="pt")

        inputs = {k: v.to(DEVICE) for k, v in inputs.items()}

        with torch.no_grad():
            outputs = model.get_video_features(
                pixel_values=inputs["pixel_values"]
            )

        # embedding
        if hasattr(outputs, "pooler_output"):
            emb = outputs.pooler_output
        else:
            emb = outputs

        emb = torch.nn.functional.normalize(emb, p=2, dim=-1)

        embeddings.append(emb.cpu().numpy())

        metadata.append({
            "video_id": row["video_id"],
            "caption": row["caption"]
        })

    except Exception as e:
        print("Error:", e)
        continue


# ============================================================
# GUARDADO FINAL
# ============================================================

embeddings = np.vstack(embeddings)

np.save(EMB_FILE, embeddings)

pd.DataFrame(metadata).to_csv(META_FILE, index=False)

print("LISTO")
print("Embeddings:", embeddings.shape)