from pathlib import Path
import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parent.parent


# CSV original balanceado
#CSV_FILE = PROJECT_ROOT / "outputs" / "sports_msr-vtt_metadata.csv"
CSV_FILE = PROJECT_ROOT / "outputs/temporales" / "sports33_msr-vtt_test_descargados.csv"

# Carpeta donde están los mp4 descargados
#VIDEO_DIR = PROJECT_ROOT / "data" / "msr-vtt" / "videos"
VIDEO_DIR = PROJECT_ROOT / "data" / "msr-vtt" / "videos-test"

# Nuevo CSV
#OUTPUT_FILE = PROJECT_ROOT / "outputs" / "sports_msr-vtt_metadata_descargados.csv"
OUTPUT_FILE = PROJECT_ROOT / "outputs" / "sports33_msr-vtt_test.csv"


# ==========================
# Leer metadata
# ==========================

df = pd.read_csv(CSV_FILE)


print("Videos en CSV original:", len(df))


# ==========================
# Obtener videos existentes
# ==========================

videos_descargados = {
    video.stem
    for video in VIDEO_DIR.glob("*.mp4")
}


print(
    "Videos encontrados en carpeta:",
    len(videos_descargados)
)


# ==========================
# Filtrar solo existentes
# ==========================

df_descargados = df[
    df["video_id"].isin(videos_descargados)
].copy()


# ==========================
# Guardar nuevo CSV
# ==========================

df_descargados.to_csv(
    OUTPUT_FILE,
    index=False
)


# ==========================
# Verificación
# ==========================

print("\nDistribución final:")
print(
    df_descargados["sport"].value_counts()
)


print(
    "\nTotal final:",
    len(df_descargados)
)


print(
    "\nArchivo generado:",
    OUTPUT_FILE
)