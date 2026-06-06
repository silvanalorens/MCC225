import json
import pandas as pd
from pathlib import Path

TRAIN_JSON = Path("data") / "activitynet" / "train.json"
TOP_N = 50
with open(TRAIN_JSON, "r", encoding="utf-8") as f:
    data = json.load(f)

rows = []

for video_id, info in data.items():

    n_captions = len(info["sentences"])
    duration = info["duration"]

    rows.append({
        "video_id": video_id,
        "duration": duration,
        "n_captions": n_captions,
        "youtube_id": video_id.replace("v_", "", 1)
    })

df = pd.DataFrame(rows)

# Filtros
df = df[
    (df["n_captions"] >= 3) &
    (df["n_captions"] <= 4) &
    (df["duration"] >= 10)
]

# Videos más cortos
df = df.sort_values("duration")

selected = df.head(TOP_N).copy()

selected["youtube_url"] = (
    "https://www.youtube.com/watch?v="
    + selected["youtube_id"]
)

Path("outputs").mkdir(exist_ok=True)

selected.to_csv(
    "outputs/activitynet_top20_short.csv",
    index=False
)

with open("outputs/urls.txt", "w", encoding="utf-8") as f:
    for url in selected["youtube_url"]:
        f.write(url + "\n")

print(f"Videos seleccionados: {len(selected)}")
print(
    selected[
        [
            "video_id",
            "duration",
            "n_captions",
            "youtube_url"
        ]
    ]
)