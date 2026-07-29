from pathlib import Path
import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parent.parent


CSV_FILE = PROJECT_ROOT / "outputs/temporales" / "sports30_msr-vtt_metadata_descargados.csv"

OUTPUT_FILE = PROJECT_ROOT / "outputs/temporales" / "sports33_msr-vtt_metadata_final.csv"


df = pd.read_csv(CSV_FILE)


print("Distribución original:")
print(df["sport"].value_counts())


# ============================
# Eliminar deportes pequeños
# ============================

MINIMO = 33

conteo = df["sport"].value_counts()

deportes_validos = conteo[
    conteo >= MINIMO
].index


df = df[
    df["sport"].isin(deportes_validos)
]


# ============================
# Balancear al mínimo común
# ============================

cantidad_final = (
    df["sport"]
    .value_counts()
    .min()
)


print(
    "\nCantidad por disciplina:",
    cantidad_final
)


lista = []

for sport, grupo in df.groupby("sport"):

    muestra = grupo.sample(
        n=cantidad_final,
        random_state=42
    )

    lista.append(muestra)


df_final = pd.concat(
    lista,
    ignore_index=True
)


# ordenar

df_final = df_final.sort_values(
    ["sport", "video_id"]
)


# guardar

df_final.to_csv(
    OUTPUT_FILE,
    index=False
)


print("\nDistribución final:")
print(df_final["sport"].value_counts())

print("\nTotal:", len(df_final))