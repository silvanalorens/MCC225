import cv2
import numpy as np

video_path = "/workspace/Semana4/ProyectoFinal/data/msr-vtt/videos/video1002.mp4"

def extract_frames(video_path, num_frames=8):
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print("No se pudo abrir el video")
        return None

    total = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    idxs = np.linspace(0, max(total - 1, 1), num_frames).astype(int)

    frames = []

    for i in idxs:
        cap.set(cv2.CAP_PROP_POS_FRAMES, i)
        ret, frame = cap.read()

        if not ret:
            continue

        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frames.append(frame)

    cap.release()

    return frames


frames = extract_frames(video_path)

print("Frames extraídos:", len(frames))
print("Shape ejemplo:", frames[0].shape if frames else None)