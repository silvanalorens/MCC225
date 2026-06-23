# ============================================================
# Prueba con un solo video usando InternVideo3-8B-Instruct
# ============================================================

import cv2
import numpy as np
import torch

from transformers import (
    AutoProcessor,
    AutoModelForCausalLM
)

# ============================================================
# CONFIGURACIÓN
# ============================================================

MODEL_NAME = "yanziang/InternVideo3-8B-Instruct"

VIDEO_PATH = (
    "/workspace/Semana4/ProyectoFinal/"
    "data/msr-vtt/videos/video1002.mp4"
)

DEVICE = (
    "cuda"
    if torch.cuda.is_available()
    else "cpu"
)

NUM_FRAMES = 8

print("Device:", DEVICE)

# ============================================================
# CARGAR MODELO
# ============================================================

print("Cargando processor...")

processor = AutoProcessor.from_pretrained(
    MODEL_NAME,
    trust_remote_code=True
)

print("Cargando modelo...")

model = AutoModelForCausalLM.from_pretrained(
    MODEL_NAME,
    trust_remote_code=True
)

model = model.to(DEVICE)
model.eval()

print("Modelo cargado.")

# ============================================================
# EXTRAER FRAMES
# ============================================================

def sample_frames(video_path, num_frames=8):

    cap = cv2.VideoCapture(video_path)

    total_frames = int(
        cap.get(cv2.CAP_PROP_FRAME_COUNT)
    )

    indices = np.linspace(
        0,
        total_frames - 1,
        num_frames
    ).astype(int)

    frames = []

    for idx in indices:

        cap.set(
            cv2.CAP_PROP_POS_FRAMES,
            idx
        )

        ok, frame = cap.read()

        if ok:

            frame = cv2.cvtColor(
                frame,
                cv2.COLOR_BGR2RGB
            )

            frames.append(frame)

    cap.release()

    return frames


frames = sample_frames(
    VIDEO_PATH,
    NUM_FRAMES
)

print("Frames extraídos:", len(frames))

# ============================================================
# PROMPT
# ============================================================

prompt = "Describe the video in detail."

# ============================================================
# PREPROCESAMIENTO
# ============================================================

inputs = processor(
    text=prompt,
    images=frames,
    return_tensors="pt"
)

inputs = {
    k: v.to(DEVICE)
    for k, v in inputs.items()
}

# ============================================================
# GENERACIÓN
# ============================================================

with torch.no_grad():

    outputs = model.generate(
        **inputs,
        max_new_tokens=128
    )

respuesta = processor.batch_decode(
    outputs,
    skip_special_tokens=True
)

print()
print("Respuesta:")
print(respuesta[0])