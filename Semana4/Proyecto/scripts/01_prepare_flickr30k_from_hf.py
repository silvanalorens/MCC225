from __future__ import annotations

import argparse
import json
import shutil
from io import BytesIO
from pathlib import Path
from typing import Any, Iterable

import pandas as pd
from PIL import Image
from datasets import Dataset, DatasetDict, load_dataset


PROJECT_ROOT = next(
    (p for p in Path(__file__).resolve().parents if (p / "src").is_dir()),
    Path(__file__).resolve().parent.parent,
)

DATASET_ALIASES = {
    # Nombre solicitado frecuentemente sin sufijo. El dataset público en HF usa "1k".
    "Vishva007/Flickr-Dataset-1": "Vishva007/Flickr-Dataset-1k",
}

SPLIT_ALIASES = {
    "train": "train",
    "training": "train",
    "val": "val",
    "valid": "val",
    "validation": "val",
    "dev": "val",
    "test": "test",
    "bootstrap": "bootstrap",
}


def _canonical_dataset_name(name: str) -> str:
    canonical = DATASET_ALIASES.get(name, name)
    if canonical != name:
        print(f"[AVISO] Dataset '{name}' no existe con ese identificador público; usando '{canonical}'.")
    return canonical


def _normalize_captions(value: Any) -> list[str]:
    if isinstance(value, list):
        return [str(x).strip() for x in value if str(x).strip()]
    if isinstance(value, tuple):
        return [str(x).strip() for x in value if str(x).strip()]
    if isinstance(value, str):
        value = value.strip()
        if not value:
            return []
        if value.startswith("["):
            try:
                loaded = json.loads(value)
                if isinstance(loaded, list):
                    return [str(x).strip() for x in loaded if str(x).strip()]
            except json.JSONDecodeError:
                pass
        return [value]
    if value is None:
        return []
    return [str(value).strip()]


def _normalize_split(value: Any, default: str = "train") -> str:
    raw = str(value or default).strip().lower()
    return SPLIT_ALIASES.get(raw, raw)


def _synthetic_split(idx: int, total: int, train_ratio: float, val_ratio: float) -> str:
    if total <= 0:
        return "train"
    frac = idx / total
    if frac < train_ratio:
        return "train"
    if frac < train_ratio + val_ratio:
        return "val"
    return "test"


def _save_image(image: Any, save_path: Path) -> None:
    save_path.parent.mkdir(parents=True, exist_ok=True)

    if isinstance(image, Image.Image):
        image.convert("RGB").save(save_path)
        return

    if isinstance(image, (str, Path)):
        with Image.open(image) as img:
            img.convert("RGB").save(save_path)
        return

    if isinstance(image, dict):
        if image.get("bytes") is not None:
            with Image.open(BytesIO(image["bytes"])) as img:
                img.convert("RGB").save(save_path)
            return
        if image.get("path") is not None:
            with Image.open(image["path"]) as img:
                img.convert("RGB").save(save_path)
            return

    raise TypeError(f"Tipo de imagen no soportado: {type(image)!r}")


def _safe_filename(row: dict[str, Any], idx: int) -> str:
    filename = str(row.get("filename") or row.get("file_name") or f"hf_{idx:06d}.jpg")
    filename = Path(filename).name
    if not filename.lower().endswith((".jpg", ".jpeg", ".png", ".webp")):
        filename = f"{filename}.jpg"
    return filename


def _row_image_id(row: dict[str, Any], idx: int) -> str:
    for key in ("img_id", "image_id", "id"):
        value = row.get(key)
        if value is not None and str(value).strip() != "":
            return f"flickr1k_{value}"
    return f"flickr1k_{idx:06d}"


def _iter_dataset_rows(ds_obj: Dataset | DatasetDict, requested_split: str) -> Iterable[tuple[str, int, dict[str, Any], int]]:
    """Yield (hf_split_name, local_index, row, split_size)."""
    if isinstance(ds_obj, DatasetDict):
        for hf_split_name, ds in ds_obj.items():
            split_size = len(ds)
            for idx, row in enumerate(ds):
                yield hf_split_name, idx, dict(row), split_size
        return

    split_size = len(ds_obj)
    for idx, row in enumerate(ds_obj):
        yield requested_split, idx, dict(row), split_size


def _load_remote_dataset(args: argparse.Namespace) -> Dataset | DatasetDict:
    dataset_name = _canonical_dataset_name(args.dataset_name)
    kwargs: dict[str, Any] = {}
    if args.trust_remote_code:
        kwargs["trust_remote_code"] = True

    if args.hf_split.lower() in {"all", "*", "datasetdict"}:
        return load_dataset(dataset_name, **kwargs)
    return load_dataset(dataset_name, split=args.hf_split, **kwargs)


def _download_from_hf(args: argparse.Namespace, out_root: Path) -> pd.DataFrame:
    dataset_name = _canonical_dataset_name(args.dataset_name)
    args.dataset_name = dataset_name
    ds_obj = _load_remote_dataset(args)
    images_dir = out_root / "images"
    images_dir.mkdir(parents=True, exist_ok=True)

    counters = {"train": 0, "val": 0, "test": 0}
    limits = {"train": args.train_limit, "val": args.val_limit, "test": args.test_limit}
    rows: list[dict[str, Any]] = []
    seen_filenames: set[str] = set()

    for hf_split_name, idx, row, split_size in _iter_dataset_rows(ds_obj, args.hf_split):
        if args.force_synthetic_splits or not row.get("split"):
            split = _synthetic_split(idx, split_size, args.train_ratio, args.val_ratio)
        else:
            split = _normalize_split(row.get("split"), default=hf_split_name)

        if split not in limits:
            continue
        if counters[split] >= limits[split]:
            continue

        caption_value = row["caption"] if "caption" in row else row.get("captions", row.get("text"))
        captions = _normalize_captions(caption_value)
        if not captions:
            continue

        image = row["image"] if "image" in row else row.get("img")
        if image is None:
            raise KeyError("La fila no contiene columna 'image' ni 'img'.")

        filename = _safe_filename(row, len(rows))
        if filename in seen_filenames:
            stem, suffix = Path(filename).stem, Path(filename).suffix
            filename = f"{stem}_{len(rows):06d}{suffix}"
        seen_filenames.add(filename)

        save_path = images_dir / filename
        _save_image(image, save_path)

        image_id = _row_image_id(row, idx)
        rows.append({
            "image_id": image_id,
            "filename": filename,
            "filepath": str(save_path.resolve()),
            "split": split,
            "caption": captions[0],
            "label": "",
            "all_captions_json": json.dumps(captions, ensure_ascii=False),
            "source_dataset": dataset_name,
            "source_hf_split": hf_split_name,
        })
        counters[split] += 1

        if all(counters[k] >= limits[k] for k in limits):
            break

    if not rows:
        raise RuntimeError("No se extrajo ningún ejemplo desde Hugging Face.")

    return pd.DataFrame(rows)


def _save_outputs(df: pd.DataFrame, out_root: Path) -> None:
    out_root.mkdir(parents=True, exist_ok=True)
    df.to_csv(out_root / "all.csv", index=False)
    for split in ["train", "val", "test", "bootstrap"]:
        split_df = df[df["split"] == split]
        if not split_df.empty:
            split_df.to_csv(out_root / f"{split}.csv", index=False)

    print("Saved:", out_root)
    print(df["split"].value_counts().to_string())
    print("Total images:", len(df))
    if "all_captions_json" in df.columns:
        n_captions = int(df["all_captions_json"].apply(lambda x: len(_normalize_captions(x))).sum())
        print("Total captions:", n_captions)


def _resolve_bootstrap_image(filepath: str, fallback_csv: Path) -> Path:
    candidates = []
    path = Path(filepath)
    if path.is_absolute():
        candidates.append(path)
    else:
        candidates.extend([
            PROJECT_ROOT / path,
            fallback_csv.parent / path.name,
            fallback_csv.parent / "images" / path.name,
        ])
    for candidate in candidates:
        if candidate.exists():
            return candidate
    raise FileNotFoundError(
        "No se encontró la imagen bootstrap referida por "
        f"{filepath!r}. Candidatos: {', '.join(str(c) for c in candidates)}"
    )


def _copy_bootstrap_dataset(fallback_csv: Path, out_root: Path) -> pd.DataFrame:
    images_dir = out_root / "images"
    images_dir.mkdir(parents=True, exist_ok=True)

    src_df = pd.read_csv(fallback_csv)
    rows: list[dict[str, Any]] = []
    for idx, row in src_df.iterrows():
        src_image = _resolve_bootstrap_image(str(row["filepath"]), fallback_csv)
        filename = str(row.get("filename") or src_image.name)
        dst_image = images_dir / filename
        shutil.copy2(src_image, dst_image)

        record = row.to_dict()
        record["image_id"] = record.get("image_id") or f"bootstrap_{idx:04d}"
        record["filename"] = filename
        record["filepath"] = str(dst_image.resolve())
        record["split"] = record.get("split") or "bootstrap"
        record["caption"] = str(record.get("caption") or "")
        record["label"] = str(record.get("label") or "")
        record["source_dataset"] = "local_bootstrap"
        rows.append(record)

    return pd.DataFrame(rows)


def main() -> None:
    parser = argparse.ArgumentParser(
        description=(
            "Prepara un subconjunto docente de Flickr desde Hugging Face. "
            "Por defecto usa Vishva007/Flickr-Dataset-1k, un dataset Parquet pequeño, "
            "sin script remoto legacy. Si la descarga falla, usa el bootstrap local."
        )
    )
    parser.add_argument("--output-root", type=str, default="data/processed/flickr1k_hf")
    parser.add_argument("--dataset-name", type=str, default="Vishva007/Flickr-Dataset-1k")
    parser.add_argument("--hf-split", type=str, default="train")
    parser.add_argument("--train-limit", type=int, default=512)
    parser.add_argument("--val-limit", type=int, default=50)
    parser.add_argument("--test-limit", type=int, default=50)
    parser.add_argument("--train-ratio", type=float, default=0.90)
    parser.add_argument("--val-ratio", type=float, default=0.05)
    parser.add_argument(
        "--force-synthetic-splits",
        action="store_true",
        help="Ignora la columna split y crea train/val/test por posición.",
    )
    parser.add_argument(
        "--trust-remote-code",
        action=argparse.BooleanOptionalAction,
        default=False,
        help="No es necesario para Vishva007/Flickr-Dataset-1k; se conserva por compatibilidad.",
    )
    parser.add_argument(
        "--fallback-bootstrap-on-error",
        action=argparse.BooleanOptionalAction,
        default=True,
        help="Usa data/bootstrap_flickr30k/metadata.csv si falla la carga remota.",
    )
    parser.add_argument(
        "--fallback-csv",
        type=str,
        default="data/bootstrap_flickr30k/metadata.csv",
    )
    args = parser.parse_args()

    if args.train_ratio <= 0 or args.val_ratio < 0 or args.train_ratio + args.val_ratio >= 1:
        raise ValueError("Los ratios deben cumplir: train_ratio > 0, val_ratio >= 0 y train_ratio + val_ratio < 1.")

    out_root = Path(args.output_root)

    try:
        df = _download_from_hf(args, out_root)
    except Exception as exc:
        if not args.fallback_bootstrap_on_error:
            raise
        print("[AVISO] No se pudo cargar Flickr desde Hugging Face.")
        print(f"[AVISO] Causa: {type(exc).__name__}: {exc}")
        print("[AVISO] Se usará el subconjunto bootstrap local para que el laboratorio siga funcionando.")
        df = _copy_bootstrap_dataset(PROJECT_ROOT / args.fallback_csv, out_root)

    _save_outputs(df, out_root)


if __name__ == "__main__":
    main()
