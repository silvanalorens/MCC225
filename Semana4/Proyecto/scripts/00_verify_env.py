from __future__ import annotations

import platform
import sys

import torch

try:
    import open_clip
    open_clip_version = getattr(open_clip, "__version__", "installed")
except Exception as e:
    open_clip_version = f"no importable: {e}"

try:
    import datasets
    datasets_version = getattr(datasets, "__version__", "installed")
except Exception as e:
    datasets_version = f"no importable: {e}"

print("Python:", sys.version)
print("Platform:", platform.platform())
print("torch.__version__ =", torch.__version__)
print("torch.version.cuda =", torch.version.cuda)
print("torch.cuda.is_available() =", torch.cuda.is_available())
print("torch.cuda.device_count() =", torch.cuda.device_count())
if torch.cuda.is_available():
    print("GPU =", torch.cuda.get_device_name(0))
print("open_clip =", open_clip_version)
print("datasets =", datasets_version)
