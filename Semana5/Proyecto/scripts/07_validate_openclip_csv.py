#!/usr/bin/env python3
from __future__ import annotations

import argparse
from pathlib import Path

import pandas as pd


def main() -> None:
    parser = argparse.ArgumentParser(description="Valida un CSV para entrenamiento OpenCLIP.")
    parser.add_argument("--csv", default="data/bootstrap_flickr30k/metadata.csv")
    parser.add_argument("--img-key", default="filepath")
    parser.add_argument("--caption-key", default="caption")
    parser.add_argument("--separator", default=",")
    args = parser.parse_args()

    csv_path = Path(args.csv)
    if not csv_path.exists():
        raise SystemExit(f"No existe el CSV: {csv_path}")

    df = pd.read_csv(csv_path, sep=args.separator)
    print("CSV:", csv_path)
    print("Separador usado:", repr(args.separator))
    print("Columnas:", list(df.columns))
    print("Filas:", len(df))

    missing = [c for c in [args.img_key, args.caption_key] if c not in df.columns]
    if missing:
        raise SystemExit(
            "Faltan columnas requeridas: " + ", ".join(missing) +
            "\nSugerencia: si tus columnas aparecen unidas en una sola columna, agrega --csv-separator ',' al entrenamiento."
        )

    bad_paths = []
    for value in df[args.img_key].head(10).astype(str):
        path = Path(value)
        if not path.is_absolute():
            path = Path.cwd() / path
        if not path.exists():
            bad_paths.append(value)

    if bad_paths:
        print("Advertencia: algunas rutas de imagen no existen, ejemplos:")
        for value in bad_paths[:5]:
            print(" -", value)
    else:
        print("Rutas de imagen OK en la muestra inicial.")

    print("CSV compatible con OpenCLIP.")


if __name__ == "__main__":
    main()
