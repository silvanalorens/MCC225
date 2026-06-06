import json
from pathlib import Path

import pandas as pd

TRAIN_JSON = Path("data/activitynet/train.json")
VIDEOS_DIR = Path("data/activitynet/videos")
OUTPUT_CSV = Path("data/activitynet/activitynet_subset.csv")


def main():

    with open(TRAIN_JSON, "r", encoding="utf-8") as f:
        annotations = json.load(f)

    rows = []

    # Obtener videos descargados
    downloaded_videos = {
        p.stem
        for p in VIDEOS_DIR.glob("*.mp4")
    }

    print(f"Videos descargados encontrados: {len(downloaded_videos)}")

    kept_videos = 0

    for video_id, info in annotations.items():

        youtube_id = video_id.replace("v_", "", 1)

        if youtube_id not in downloaded_videos:
            continue

        kept_videos += 1

        timestamps = info["timestamps"]
        sentences = info["sentences"]
        duration = info["duration"]

        for idx, (ts, sentence) in enumerate(
            zip(timestamps, sentences)
        ):

            rows.append(
                {
                    "video_id": video_id,
                    "youtube_id": youtube_id,
                    "video_file": f"{youtube_id}.mp4",
                    "duration": duration,
                    "segment_id": idx,
                    "start": ts[0],
                    "end": ts[1],
                    "caption": sentence,
                }
            )

    df = pd.DataFrame(rows)

    OUTPUT_CSV.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    df.to_csv(
        OUTPUT_CSV,
        index=False
    )

    print()
    print(f"Videos conservados: {kept_videos}")
    print(f"Segmentos creados: {len(df)}")
    print(f"CSV generado: {OUTPUT_CSV}")

    print()
    print(df.head())


if __name__ == "__main__":
    main()