from pathlib import Path

video_dir = Path("/workspace/Semana4/ProyectoFinal/data/MSR-VTT/videos")

videos = sorted(video_dir.glob("*.mp4"))

print(f"Se encontraron {len(videos)} videos")

for video_path in videos:
    print(video_path)