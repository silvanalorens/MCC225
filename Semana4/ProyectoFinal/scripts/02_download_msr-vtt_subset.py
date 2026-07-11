from pathlib import Path
import pandas as pd
import subprocess

PROJECT_ROOT = Path(__file__).resolve().parent.parent

VIDEO_DIR = PROJECT_ROOT /"data"/"msr-vtt"/"videos"
VIDEO_DIR.mkdir(parents=True, exist_ok=True)
CSV_FILE = PROJECT_ROOT / "outputs" / "sports_subset_2.csv"
df = pd.read_csv(
    CSV_FILE
)

for i, row in df.iterrows():

    video_id = row["video_id"]
    url = row["url"]

    output_file = VIDEO_DIR / f"{video_id}.mp4"

    if output_file.exists():
        print(f"{video_id} ya existe")
        continue

    print(f"[{i+1}/{len(df)}] descargando {video_id}")

    cmd = [
        "yt-dlp",
        "-f",
        "mp4",
        "-o",
        str(output_file),
        url
    ]

    try:
       subprocess.run(cmd, check=True)

    except subprocess.CalledProcessError as e:
       print(f"No se pudo descargar {video_id}")
       print(e)