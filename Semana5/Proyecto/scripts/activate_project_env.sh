#!/usr/bin/env bash
# Uso: source scripts/activate_project_env.sh
# Define la raíz del proyecto como PYTHONPATH para que Python encuentre src/.
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "${SCRIPT_DIR}/.." && pwd)"
cd "${PROJECT_ROOT}"
export PYTHONPATH="${PROJECT_ROOT}:${PYTHONPATH:-}"
echo "PROJECT_ROOT=${PROJECT_ROOT}"
echo "PYTHONPATH=${PYTHONPATH}"
