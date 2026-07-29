from pathlib import Path

from datasets import load_dataset
import pandas as pd


# =====================================================
# RUTAS
# =====================================================

PROJECT_ROOT = Path(__file__).resolve().parent.parent

OUTPUT_DIR = PROJECT_ROOT / "outputs"
OUTPUT_DIR.mkdir(exist_ok=True)

OUTPUT_CSV = OUTPUT_DIR / "sports33_msr-vtt_test.csv"



# =====================================================
# CONFIGURACIÓN
# =====================================================

VIDEOS_PER_SPORT = 40


SPORT_KEYWORDS = {

    "basketball": {
        "basketball":5,
        "basket ball":5,
        "nba":4,
        "dunk":4,
        "hoop":3,
        "court":1,
        "player":1
    },

    "soccer": {
        "soccer":5,
        "football match":5,
        "soccer player":5,
        "goal":4,
        "goalkeeper":4,
        "kick":3,
        "stadium":2
    },

    "tennis": {
        "tennis":5,
        "tennis player":5,
        "tennis match":5,
        "racket":4,
        "serve":4,
        "court":2
    },

    "swimming": {
        "swimming":5,
        "swimmer":5,
        "swimming pool":5,
        "swim":4,
        "race":2,
        "olympic":3
    },

    "golf": {
        "golf":5,
        "golfer":5,
        "golf course":5,
        "golf club":4,
        "putt":4,
        "swing":2
    }

}
# Leer train.csv

train_df = pd.read_csv(OUTPUT_DIR / "sports33_msr-vtt_train.csv")

train_ids = set(train_df["video_id"])

# =====================================================
# CARGAR DATASET
# =====================================================

print("Cargando MSR-VTT...")

dataset = load_dataset(
    "friedrichor/MSR-VTT",
    "train_9k"
)["train"]

print("Videos:", len(dataset))

print("\nColumnas:")
print(dataset.column_names)

print("\nPrimer ejemplo:")
print(dataset[0])


# =====================================================
# CALCULAR SCORES
# =====================================================

candidates = []

for sample in dataset:
    if sample["video_id"] in train_ids:
       continue

    caption = sample["caption"]

    if isinstance(caption, list):
        captions = " ".join(caption).lower()
        captions_save = " ||| ".join(caption)
    else:
        captions = str(caption).lower()
        captions_save = str(caption)

    scores = {sport:0 for sport in SPORT_KEYWORDS}

    for sport, keywords in SPORT_KEYWORDS.items():

        for word, weight in keywords.items():

            if word in captions:
                scores[sport] += weight

    best_sport = max(scores, key=scores.get)
    best_score = scores[best_sport]

    if best_score < 5:
        continue

    candidates.append({

        "sport": best_sport,

        "score": best_score,

        "video_id": sample.get("video_id", ""),

        "video": sample.get("video", ""),

        "url": sample.get("url", ""),

        "start_time": sample.get("start time", None),

        "end_time": sample.get("end time", None),

        "category": sample.get("category", None),

        "captions": captions_save

    })


print("\nNúmero de candidatos:", len(candidates))

if len(candidates) == 0:
    raise RuntimeError(
        "No se encontró ningún video. Revisa el contenido de dataset[0]."
    )


df = pd.DataFrame(candidates)

print("\nCandidatos por deporte:")
print(df.groupby("sport").size())


# =====================================================
# SELECCIÓN BALANCEADA
# =====================================================

final = []

for sport in SPORT_KEYWORDS.keys():

    subset = (
        df[df["sport"] == sport]
        .sort_values(
            "score",
            ascending=False
        )
        .head(VIDEOS_PER_SPORT)
    )

    final.append(subset)


final_df = pd.concat(final, ignore_index=True)

print("\nDataset final:")
print(final_df.groupby("sport").size())


# =====================================================
# GUARDAR
# =====================================================

final_df.to_csv(
    OUTPUT_CSV,
    index=False
)

print("\nGuardado:", OUTPUT_CSV)