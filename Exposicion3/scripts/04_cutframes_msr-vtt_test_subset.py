#pip install opencv-python-headless
from pathlib import Path
import pandas as pd
import cv2
from tqdm import tqdm


PROJECT_ROOT = Path(__file__).resolve().parent.parent


# ==========================
# Archivos
# ==========================

CSV_FILE = (
    PROJECT_ROOT /
    "outputs" /
    "sports33_msr-vtt_test.csv"
)


VIDEO_DIR = (
    PROJECT_ROOT /
    "data" /
    "msr-vtt" /
    "videos-test"
)


FRAME_ROOT = (
    PROJECT_ROOT /
    "data" /
    "msr-vtt" /
    "frames-test"
)


FRAME_ROOT.mkdir(
    parents=True,
    exist_ok=True
)


# ==========================
# Contextos temporales
# ==========================

CONTEXTOS = {
    12: "context_12"
}


# ==========================
# Leer CSV
# ==========================

df = pd.read_csv(CSV_FILE)


print(
    "Videos-test:",
    len(df)
)


# ==========================
# Función extracción
# ==========================

def extract_frames(
    video_path,
    output_dir,
    video_id,
    start_time,
    end_time,
    num_frames
):

    output_dir.mkdir(
        parents=True,
        exist_ok=True
    )


    cap = cv2.VideoCapture(
        str(video_path)
    )


    fps = cap.get(
        cv2.CAP_PROP_FPS
    )


    if fps == 0:
        cap.release()
        return 0


    start_frame = int(
        float(start_time) * fps
    )

    end_frame = int(
        float(end_time) * fps
    )


    total_frames = end_frame - start_frame


    if total_frames <= 0:
        cap.release()
        return 0


    # selección uniforme

    indexes = [
        int(
            start_frame +
            i * total_frames / num_frames
        )
        for i in range(num_frames)
    ]


    saved = 0


    for idx in indexes:

        cap.set(
            cv2.CAP_PROP_POS_FRAMES,
            idx
        )


        ret, frame = cap.read()


        if not ret:
            continue


        filename = (
            output_dir /
            f"{video_id}_frame_{saved:03d}.jpg"
        )


        cv2.imwrite(
            str(filename),
            frame
        )


        saved += 1


    cap.release()

    return saved



# ==========================
# Procesamiento
# ==========================

for _, row in tqdm(
    df.iterrows(),
    total=len(df)
):

    video_id = row["video_id"]
    sport = row["sport"]


    video_path = (
        VIDEO_DIR /
        f"{video_id}.mp4"
    )


    if not video_path.exists():

        print(
            "No existe:",
            video_id
        )

        continue


    # crear cada contexto

    for num_frames, folder in CONTEXTOS.items():


        output_dir = (
            FRAME_ROOT /
            folder /
            sport
        )


        # evitar repetir

        existentes = list(
            output_dir.glob(
                f"{video_id}_frame_*.jpg"
            )
        )


        if len(existentes) >= num_frames:
            continue


        extract_frames(
            video_path,
            output_dir,
            video_id,
            row["start_time"],
            row["end_time"],
            num_frames
        )


print("\nExtracción finalizada")