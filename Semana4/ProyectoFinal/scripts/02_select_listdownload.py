import pandas as pd

df = pd.read_csv("outputs/activitynet_top20_short.csv")

df["youtube_url"].to_csv(
    "urls.txt",
    index=False,
    header=False
)