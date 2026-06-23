from __future__ import annotations

import csv
import urllib.request
from pathlib import Path


def fetch_assets_from_manifest(manifest_path: Path) -> None:
    """Descarga activos remotos a partir de un manifest simple."""
    with manifest_path.open("r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            url = row.get("image_url")
            dst = row.get("image_path")
            if not url or not dst:
                continue
            dst_path = Path(dst)
            dst_path.parent.mkdir(parents=True, exist_ok=True)
            if dst_path.exists():
                continue
            print(f"Descargando {url} -> {dst}")
            urllib.request.urlretrieve(url, dst)


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Proporciona un manifest con columnas image_url e image_path para usar este helper.")
        raise SystemExit(1)
    fetch_assets_from_manifest(Path(sys.argv[1]))
