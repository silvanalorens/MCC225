from pathlib import Path
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parent.parent

VIDEO_DIR = PROJECT_ROOT / "data" / "msr-vtt" / "videos"
OUTPUT_DIR = PROJECT_ROOT / "outputs"
OUTPUT_DIR.mkdir(exist_ok=True)

subset_csv = OUTPUT_DIR / "sports_subset.csv"


df1 = pd.read_csv(subset_csv)
df2 = pd.read_csv(OUTPUT_DIR / "sports_subset_2.csv")

df = pd.concat([df1, df2], ignore_index=True)
df = df.drop_duplicates("video_id")
rows = []
for _, row in df.iterrows():


    video_id = row["video_id"]
    caption = row["caption"]

    video_path = VIDEO_DIR / f"{video_id}.mp4"

    if video_path.exists():

        rows.append(
            {
                "video_id": video_id,
                "video_path": str(video_path),
                "caption": caption
            }
        )


metadata = pd.DataFrame(rows)

metadata.to_csv(
OUTPUT_DIR / "sports_msr-vtt_metadata.csv",
index=False
)

print(metadata.head())
print()
print("Videos válidos:", len(metadata))
