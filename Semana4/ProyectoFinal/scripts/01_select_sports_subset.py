import pandas as pd
from datasets import load_dataset
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
OUTPUT_DIR = PROJECT_ROOT / "outputs"

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

sports_keywords = [
"soccer",
"football",
"basketball",
"tennis",
"baseball",
"swimming",
"volleyball",
"golf",
"boxing",
"running",
"cycling",
"surfing",
"skiing"
]

ds = load_dataset("AlexZigma/msr-vtt")

rows = []


for sample in ds["train"]:

   caption = sample["caption"].lower()

   if any(k in caption for k in sports_keywords):
    rows.append(
        {
            "video_id": sample["video_id"],
            "caption": sample["caption"],
            "url": sample["url"]
        }
    )


df = pd.DataFrame(rows)

# un video por id

df = df.drop_duplicates("video_id")

# tomar 100 videos

df = df.iloc[100:200]

df.to_csv(
    OUTPUT_DIR / "sports_subset_2.csv",
    index=False
)

print(df.head())
print("Videos:", len(df))
