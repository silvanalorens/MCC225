from pathlib import Path
import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parent.parent

#muestra principal
#CSV_FILE = PROJECT_ROOT / "outputs/temporales" / "sports33_msr-vtt_metadata_descargados.csv"

#muestra de prueba
CSV_FILE = PROJECT_ROOT / "outputs/temporales" / "sports33_msr-vtt_test_descargados.csv"

# estandarizar misma cantidad muestra principal
#OUTPUT_FILE = PROJECT_ROOT / "outputs/temporales" / "sports33_msr-vtt_metadata_final.csv"

# estandarizar muestra de prueba
OUTPUT_FILE = PROJECT_ROOT / "outputs/temporales" / "sports33_msr-vtt_test_final.csv"

df = pd.read_csv(CSV_FILE)


print("Distribución original:")
print(df["sport"].value_counts())

# ============================
# Eliminar deportes pequeños
# ============================

MINIMO = 13

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

#cantidad_final = (
#    df["sport"]
#    .value_counts()
#    .min()
#)

#muestra de prueba
cantidad_final = 10
print(
    "\nCantidad por disciplina:",
    cantidad_final
)


lista = []

for sport, grupo in df.groupby("sport"):

    if len(grupo) < cantidad_final:

        print(
            f"Advertencia: {sport} solo tiene {len(grupo)} videos."
        )

        continue

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