import pandas as pd

df = pd.read_csv(
    "outputs/sports33_msr-vtt_metadata_final.csv"
)

df["duration"] = (
    df["end_time"] -
    df["start_time"]
)

print(df["duration"].describe())