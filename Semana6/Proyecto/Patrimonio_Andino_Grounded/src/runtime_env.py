from __future__ import annotations

from pathlib import Path
from typing import Dict
import os


def _candidate_roots(start: Path) -> list[Path]:
    """Genera candidatos desde el directorio actual hacia arriba."""
    return [start.resolve(), *start.resolve().parents]


def detect_project_root(start: Path | None = None) -> Path:
    """Detecta la raíz del proyecto con prioridad para la estructura MCC225/Semana6/Proyecto."""
    current = (start or Path.cwd()).resolve()

    # Prioridad 1: coincidencia exacta dentro del contenedor del curso.
    expected = Path('/workspace') / 'Semana6' / 'Proyecto' / 'Patrimonio_Andino_Grounded'
    if (expected / 'data_processed' / 'records_master.jsonl').exists() and (expected / 'notebooks').exists():
        return expected

    # Prioridad 2: búsqueda ascendente estándar.
    for base in _candidate_roots(current):
        if (base / 'data_processed' / 'records_master.jsonl').exists() and (base / 'notebooks').exists():
            return base

    # Prioridad 3: si el usuario abrió Jupyter en /workspace, intenta la ruta esperada.
    if str(current).startswith('/workspace') and expected.exists():
        return expected

    return current


def collect_runtime_report(project_root: Path) -> Dict[str, str]:
    """Devuelve un reporte breve del entorno de ejecución."""
    report = {
        'cwd': str(Path.cwd().resolve()),
        'project_root': str(project_root),
        'expected_root': str(Path('/workspace') / 'Semana6' / 'Proyecto' / 'Patrimonio_Andino_Grounded'),
        'in_workspace': str(str(project_root).startswith('/workspace')),
        'records_master': str((project_root / 'data_processed' / 'records_master.jsonl').exists()),
        'jupyter_port': os.environ.get('JUPYTER_PORT', '8899'),
        'python_executable': os.environ.get('PYTHON_EXECUTABLE', ''),
    }
    try:
        import torch
        report['torch_version'] = torch.__version__
        report['cuda_available'] = str(torch.cuda.is_available())
        report['cuda_device_count'] = str(torch.cuda.device_count())
        if torch.cuda.is_available():
            report['cuda_device_name_0'] = torch.cuda.get_device_name(0)
    except Exception as exc:  # pragma: no cover
        report['torch_error'] = str(exc)
    return report


def recommended_notebook_order() -> list[str]:
    """Orden sugerido de ejecución dentro del curso."""
    return [
        '10_verificacion_entorno_docker_linux.ipynb',
        '07_demo_integrada_y_modelo_real_opcional.ipynb',
        '08_corrida_local_rtx4080_opcional.ipynb',
        '09_casos_comentados_en_profundidad.ipynb',
    ]
