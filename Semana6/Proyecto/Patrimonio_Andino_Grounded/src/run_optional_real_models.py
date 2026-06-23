from __future__ import annotations

import json
from pathlib import Path


def main() -> None:
    # Este script deja constancia del modo de ejecución opcional.
    payload = {
        "mensaje": "Ruta opcional para modelos reales preparada.",
        "nota": "Usa los notebooks 08 o 10 para verificar GPU y activos locales.",
        "cwd": str(Path.cwd().resolve()),
    }
    print(json.dumps(payload, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
