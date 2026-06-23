#!/usr/bin/env bash
set -euo pipefail

PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
IMAGE="${MCC225_IMAGE:-mcc225_gpu:latest}"

cd "${PROJECT_ROOT}"

echo "Validando Docker + GPU para ejecución sin Kubernetes"
echo "PROJECT_ROOT=${PROJECT_ROOT}"
echo "IMAGE=${IMAGE}"

echo
if ! command -v docker >/dev/null 2>&1; then
  echo "ERROR: docker no está instalado o no está en PATH." >&2
  exit 1
fi

echo "Docker OK: $(docker --version)"

echo
if command -v nvidia-smi >/dev/null 2>&1; then
  echo "Host NVIDIA OK"
  nvidia-smi | head -20
else
  echo "ADVERTENCIA: nvidia-smi no está disponible en el host." >&2
  echo "Si vas a usar GPU, revisa el driver NVIDIA y NVIDIA Container Toolkit." >&2
fi

echo
if ! docker image inspect "${IMAGE}" >/dev/null 2>&1; then
  echo "ERROR: no existe la imagen Docker ${IMAGE}." >&2
  echo "Construye la imagen del curso o define MCC225_IMAGE con el nombre correcto." >&2
  exit 2
fi

echo "Imagen Docker OK: ${IMAGE}"

echo
echo "Probando GPU dentro del contenedor"
docker run --rm --gpus all \
  -v "${PROJECT_ROOT}:/workspace/Proyecto" \
  -w /workspace/Proyecto \
  "${IMAGE}" \
  bash -lc 'python - <<PY
import importlib
import sys

try:
    import torch
    print("torch.__version__ =", torch.__version__)
    print("torch.version.cuda =", torch.version.cuda)
    print("torch.cuda.is_available() =", torch.cuda.is_available())
    print("torch.cuda.device_count() =", torch.cuda.device_count())
    if torch.cuda.is_available():
        print("GPU =", torch.cuda.get_device_name(0))
except Exception as exc:
    print("Torch check failed:", exc)
    sys.exit(1)

for mod in ["open_clip", "pandas", "yaml"]:
    try:
        importlib.import_module(mod)
        print(f"{mod}: OK")
    except Exception as exc:
        print(f"{mod}: FALTA -> {exc}")
PY'
