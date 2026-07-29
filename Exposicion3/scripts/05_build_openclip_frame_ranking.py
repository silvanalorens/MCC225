import os
import json
import torch
import pandas as pd
import numpy as np
from PIL import Image
from tqdm import tqdm
import open_clip
from pathlib import Path


# ============================
# CONFIGURACIÓN
# ============================

MODEL_NAME = "ViT-B-32"
PRETRAINED = "openai"

DEVICE = "cuda" if torch.cuda.is_available() else "cpu"

VIDEO_DIR = Path("videos")
FRAME_DIR = Path("frames")

CSV_PATH = "sports_msr-vtt_metadata30.csv"

OUTPUT_FILE = "openclip_frame_ranking.json"

TOP_K = 16


# ============================
# CARGAR MODELO OPENCLIP
# ============================

print("Cargando OpenCLIP...")

model, _, preprocess = open_clip.create_model_and_transforms(
    MODEL_NAME,
    pretrained=PRETRAINED
)

tokenizer = open_clip.get_tokenizer(MODEL_NAME)

model = model.to(DEVICE)
model.eval()


# ============================
# FUNCIONES
# ============================

@torch.no_grad()
def encode_image(image_path):

    image = Image.open(image_path).convert("RGB")

    image_tensor = preprocess(image)
    image_tensor = image_tensor.unsqueeze(0)
    image_tensor = image_tensor.to(DEVICE)

    embedding = model.encode_image(image_tensor)

    embedding = embedding / embedding.norm(
        dim=-1,
        keepdim=True
    )

    return embedding.cpu()


@torch.no_grad()
def encode_text(text):

    tokens = tokenizer([text])

    tokens = tokens.to(DEVICE)

    embedding = model.encode_text(tokens)

    embedding = embedding / embedding.norm(
        dim=-1,
        keepdim=True
    )

    return embedding.cpu()


def cosine_similarity(a, b):

    return float(
        (a @ b.T).item()
    )


# ============================
# CARGAR DATASET
# ============================

print("Leyendo CSV...")

df = pd.read_csv(
    CSV_PATH
)

print(
    "Videos encontrados:",
    len(df)
)


# ============================
# PROCESAMIENTO
# ============================

results = []


for idx, row in tqdm(
    df.iterrows(),
    total=len(df)
):

    video_id = row["video_id"]

    caption = row["captions"]


    frame_path = FRAME_DIR / video_id


    if not frame_path.exists():
        continue


    text_embedding = encode_text(
        caption
    )


    frame_scores = []


    frames = sorted(
        frame_path.glob(
            "*.jpg"
        )
    )


    for frame in frames:

        image_embedding = encode_image(
            frame
        )

        score = cosine_similarity(
            image_embedding,
            text_embedding
        )


        frame_scores.append(
            {
                "frame": str(frame),
                "score": score
            }
        )


    frame_scores = sorted(
        frame_scores,
        key=lambda x: x["score"],
        reverse=True
    )


    selected_frames = frame_scores[:TOP_K]


    results.append(
        {
            "video_id": video_id,
            "caption": caption,
            "frames": selected_frames
        }
    )


print(
    "Procesamiento terminado"
)
# ============================
# GUARDAR RESULTADOS
# ============================

with open(
    OUTPUT_FILE,
    "w",
    encoding="utf-8"
) as f:

    json.dump(
        results,
        f,
        indent=4,
        ensure_ascii=False
    )


print(
    "Archivo generado:",
    OUTPUT_FILE
)


# ============================
# CREAR DATASET PARA MODELOS
# VISUALBERT / VILBERT
# ============================


visualbert_dataset = []


for item in results:

    video_id = item["video_id"]

    caption = item["caption"]


    frames = []


    for frame_data in item["frames"]:

        frames.append(
            {
                "image": frame_data["frame"],
                "score": frame_data["score"]
            }
        )


    visualbert_dataset.append(
        {
            "video_id": video_id,
            "text": caption,
            "images": frames
        }
    )


VISUAL_OUTPUT = (
    "visualbert_vilbert_dataset.json"
)


with open(
    VISUAL_OUTPUT,
    "w",
    encoding="utf-8"
) as f:

    json.dump(
        visualbert_dataset,
        f,
        indent=4,
        ensure_ascii=False
    )


print(
    "Dataset multimodal generado:",
    VISUAL_OUTPUT
)
# ============================
# ESTADÍSTICAS
# ============================

total_videos = len(results)

total_frames = 0


for item in results:

    total_frames += len(
        item["frames"]
    )


print("==============================")
print("ESTADÍSTICAS")
print("==============================")

print(
    "Videos procesados:",
    total_videos
)

print(
    "Frames seleccionados:",
    total_frames
)

print(
    "Promedio frames/video:",
    total_frames / total_videos
)


# ============================
# MOSTRAR EJEMPLO
# ============================

if len(results) > 0:

    example = results[0]


    print("\nEjemplo:")
    print(
        "Video:",
        example["video_id"]
    )

    print(
        "Texto:",
        example["caption"]
    )


    print(
        "\nFrames seleccionados:"
    )


    for frame in example["frames"]:

        print(
            frame["frame"],
            frame["score"]
        )

import json


def load_multimodal_dataset(
    path
):

    with open(
        path,
        "r",
        encoding="utf-8"
    ) as f:

        data = json.load(f)


    return data



dataset = load_multimodal_dataset(
    "visualbert_vilbert_dataset.json"
)


print(
    "Elementos cargados:",
    len(dataset)
)


sample = dataset[0]


print(
    sample["video_id"]
)

print(
    sample["text"]
)

print(
    len(sample["images"])
)