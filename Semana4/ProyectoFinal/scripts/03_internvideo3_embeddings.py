import torch
import cv2
import numpy as np
from pathlib import Path
from transformers import AutoModelForCausalLM, AutoProcessor

# ============================================================
# CONFIGURACIÓN GENERAL
# ============================================================

BASE_DIR = "/workspace/Semana4/ProyectoFinal"

# Carpeta de videos MSR-VTT
VIDEO_DIR = Path(f"{BASE_DIR}/data/MSR-VTT/videos")

# Carpeta de salida para embeddings
OUTPUT_DIR = Path(f"{BASE_DIR}/outputs/internvideo3_embeddings")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Modelo InternVideo3
MODEL_NAME = "yanziang/InternVideo3-8B-Instruct"

# Dispositivo (CPU o GPU)
DEVICE = "cuda" if torch.cuda.is_available() else "cpu"

# Número de frames por video
NUM_FRAMES = 8

print("Dispositivo:", DEVICE)

# ============================================================
# CARGA DEL MODELO Y PROCESSOR
# ============================================================

print("Cargando modelo...")

model = AutoModelForCausalLM.from_pretrained(
    MODEL_NAME,
    trust_remote_code=True,
).to(DEVICE)

processor = AutoProcessor.from_pretrained(
    MODEL_NAME,
    trust_remote_code=True,
)

print("Modelo cargado correctamente.")

# ============================================================
# FUNCIÓN: MUESTREO DE FRAMES DEL VIDEO
# ============================================================

def sample_frames(video_path, num_frames=8):
    """
    Extrae frames uniformemente distribuidos del video.
    """

    cap = cv2.VideoCapture(str(video_path))

    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    if total_frames <= 0:
        cap.release()
        return []

    indices = np.linspace(0, total_frames - 1, num_frames).astype(int)

    frames = []

    for idx in indices:
        cap.set(cv2.CAP_PROP_POS_FRAMES, idx)
        ok, frame = cap.read()

        if ok:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frames.append(frame)

    cap.release()

    return frames

# ============================================================
# LISTA DE VIDEOS
# ============================================================

videos = sorted(VIDEO_DIR.glob("*.mp4"))

total_videos = len(videos)

print("Total de videos:", total_videos)

# ============================================================
# LISTA PARA CONTROL (opcional)
# ============================================================

video_names = []

# ============================================================
# LOOP PRINCIPAL
# ============================================================

for i, video_path in enumerate(videos):

    print(f"[{i+1}/{total_videos}] {video_path.name}")

    try:
        # --------------------------------------------------------
        # 1. Extraer frames del video
        # --------------------------------------------------------
        frames = sample_frames(video_path, NUM_FRAMES)

        # --------------------------------------------------------
        # 2. Construir prompt multimodal
        # --------------------------------------------------------
        messages = [
            {
                "role": "user",
                "content": [
                    {"type": "video", "video": str(video_path), "fps": 1},
                    {"type": "text", "text": "Represent this video."},
                ],
            }
        ]

        text = processor.apply_chat_template(
            messages,
            tokenize=False,
            add_generation_prompt=True,
            enable_thinking=True
        )

        # --------------------------------------------------------
        # 3. Preprocesamiento
        # --------------------------------------------------------
        inputs = processor(
            text=text,
            images=frames,
            return_tensors="pt"
        ).to(DEVICE)

        # --------------------------------------------------------
        # 4. Forward pass (sin generación de texto)
        # --------------------------------------------------------
        with torch.no_grad():
            outputs = model(**inputs)

            # Representación del modelo (logits promedio)
            logits = outputs.logits
            embedding = logits.mean(dim=1).squeeze()

        # --------------------------------------------------------
        # 5. Guardar embedding individual
        # --------------------------------------------------------
        save_path = OUTPUT_DIR / f"{video_path.stem}.npy"

        np.save(save_path, embedding.cpu().numpy())

        video_names.append(video_path.name)

    except Exception as e:
        print(f"Error en {video_path.name}: {e}")
        continue

print("Proceso terminado.")
print("Embeddings guardados en:", OUTPUT_DIR)