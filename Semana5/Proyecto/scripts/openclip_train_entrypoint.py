from __future__ import annotations

"""Entrada estable para torchrun.

Permite ejecutar OpenCLIP training como script posicional de torchrun para que
argumentos como --logs, --name o --precision sean interpretados por
open_clip_train.main y no por torchrun.
"""

import runpy

if __name__ == "__main__":
    runpy.run_module("open_clip_train.main", run_name="__main__")
