from datasets import load_dataset
import pandas as pd

ds = load_dataset("AlexZigma/msr-vtt")

df = pd.DataFrame(ds["train"])

print(df.columns)

print(df.groupby("video_id").size().describe())

print(df.groupby("video_id").size().value_counts().sort_index())