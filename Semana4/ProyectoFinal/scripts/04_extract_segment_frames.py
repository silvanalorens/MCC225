from __future__ import annotations

import argparse
from pathlib import Path

import cv2
import pandas as pd
from tqdm import tqdm


def extract_frame_at_time(cap: cv2.VideoCapture, time_sec: float):
    cap.set(cv2.CAP_PROP_POS_MSEC, time_sec * 1000)
    success, frame = cap.read()

    if not success:
        return None

    return frame


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--metadata-csv",
        default="data/activitynet/activitynet_subset.csv",
    )

    parser.add_argument(
        "--videos-dir",
        default="data/activitynet/videos",
    )

    parser.add_argument(
        "--frames-dir",
        default="data/activitynet/frames",
    )

    parser.add_argument(
        "--frames-per-segment",
        type=int,
        default=5,
    )

    parser.add_argument(
        "--output-csv",
        default="data/activitynet/activitynet_frames.csv",
    )

    args = parser.parse_args()

    metadata_csv = Path(args.metadata_csv)
    videos_dir = Path(args.videos_dir)
    frames_dir = Path(args.frames_dir)

    frames_dir.mkdir(parents=True, exist_ok=True)

    df = pd.read_csv(metadata_csv)

    records = []

    for _, row in tqdm(df.iterrows(), total=len(df)):
        video_file = row["video_file"]
        video_path = videos_dir / video_file

        if not video_path.exists():
            print(f"[WARN] No existe: {video_path}")
            continue

        start_time = float(row["start"])
        end_time = float(row["end"])

        duration = max(end_time - start_time, 0.01)

        cap = cv2.VideoCapture(str(video_path))

        if not cap.isOpened():
            print(f"[WARN] No se pudo abrir: {video_path}")
            continue

        for frame_idx in range(args.frames_per_segment):

            if args.frames_per_segment == 1:
                t = (start_time + end_time) / 2
            else:
                alpha = frame_idx / (args.frames_per_segment - 1)
                t = start_time + alpha * duration

            frame = extract_frame_at_time(cap, t)

            if frame is None:
                continue

            image_name = (
                f"{row['youtube_id']}"
                f"_seg{row['segment_id']}"
                f"_f{frame_idx}.jpg"
            )

            image_path = frames_dir / image_name

            cv2.imwrite(str(image_path), frame)

            records.append(
                {
                    "video_id": row["video_id"],
                    "youtube_id": row["youtube_id"],
                    "segment_id": row["segment_id"],
                    "start": start_time,
                    "end": end_time,
                    "caption": row["caption"],
                    "frame_idx": frame_idx,
                    "frame_path": str(image_path.resolve()),
                }
            )

        cap.release()

    out_df = pd.DataFrame(records)
    out_df.to_csv(args.output_csv, index=False)

    print()
    print("Frames extraídos:", len(out_df))
    print("CSV guardado en:", args.output_csv)


if __name__ == "__main__":
    main()