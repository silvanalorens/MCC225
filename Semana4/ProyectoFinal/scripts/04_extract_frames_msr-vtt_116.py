from pathlib import Path
import cv2
import pandas as pd
from tqdm import tqdm


def extract_frame_at_index(cap, frame_idx):

    cap.set(cv2.CAP_PROP_POS_FRAMES, frame_idx)

    success, frame = cap.read()

    if not success:
        return None

    return frame


def extract_frames(video_path, output_dir, num_frames=8):

    cap = cv2.VideoCapture(str(video_path))

    if not cap.isOpened():
        return []

    total_frames = int(
        cap.get(cv2.CAP_PROP_FRAME_COUNT)
    )

    frame_indexes = [
        int(i * total_frames / num_frames)
        for i in range(num_frames)
    ]

    video_id = video_path.stem

    video_frames = []

    video_dir = output_dir / video_id
    video_dir.mkdir(
        parents=True,
        exist_ok=True
    )

    for idx, frame_number in enumerate(frame_indexes):

        frame = extract_frame_at_index(
            cap,
            frame_number
        )

        if frame is None:
            continue

        image_path = (
            video_dir /
            f"frame_{idx}.jpg"
        )

        cv2.imwrite(
            str(image_path),
            frame
        )

        video_frames.append(
            {
                "video_id": video_id,
                "frame_idx": idx,
                "frame_path": str(
                    image_path.resolve()
                )
            }
        )

    cap.release()

    return video_frames