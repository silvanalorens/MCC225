### Semana 4: OpenCLIP para aprendizaje contrastivo imagen-texto

Este proyecto implementa un laboratorio reproducible de Semana 4 para trabajar aprendizaje contrastivo imagen-texto con OpenCLIP. El énfasis está en construcción de embeddings, recuperación cruzada, evaluación con métricas de ranking, análisis de negativos duros y una evaluación zero-shot simple.

> Este proyecto está pensado para ejecutarse dentro del contenedor Docker del repositorio MCC225. No está planteado como una solución local aislada.

#### 1. Propósito académico

La semana 4 del curso trabaja aprendizaje contrastivo, alineamiento entre modalidades y recuperación cruzada. Este proyecto cubre ese objetivo mediante un flujo completo con OpenCLIP:

1. verificación del entorno dentro del contenedor,
2. carga de un checkpoint preentrenado de OpenCLIP,
3. preparación de un conjunto pequeño de imágenes y captions,
4. codificación de imágenes y textos en un espacio común,
5. evaluación de recuperación imagen a texto y texto a imagen,
6. minería de negativos duros,
7. evaluación zero-shot simple sobre el bootstrap local,
8. preparación opcional de un subconjunto Flickr1k desde Hugging Face.

El objetivo no es maximizar desempeño en un benchmark grande. El objetivo es mostrar de forma controlada y verificable cómo se diseña, ejecuta, evalúa y discute un pipeline contrastivo multimodal.

#### 2. Alcance del laboratorio

Incluido:

* Notebook principal: `Cuaderno9-MCC225.ipynb`
* Scripts modulares en `scripts/`
* Código reutilizable en `src/`
* Configuraciones en `configs/`
* Dataset bootstrap pequeño en `data/bootstrap_flickr30k/`
* Preparación opcional de `Vishva007/Flickr-Dataset-1k`
* Métricas generadas en `outputs/metrics/`
* Embeddings generados en `outputs/embeddings/`
* Plantillas de ejecución local dentro del contenedor
* Plantillas opcionales para `torchrun` y SLURM.

No incluido como objetivo principal:

* entrenamiento serio a gran escala,
* evaluación estadísticamente concluyente con el bootstrap pequeño.
* despliegue productivo,
* Kubernetes,
* fine-tuning profundo de modelos fundacionales.

#### 3. Estructura del proyecto

```text
Semana4/
├── papers/
└── Proyecto/
    ├── Cuaderno9-MCC225.ipynb
    ├── README.md
    ├── requirements-extra.txt
    ├── pyproject.toml
    ├── configs/
    ├── data/
    │   ├── bootstrap_flickr30k/
    │   └── processed/
    ├── outputs/
    │   ├── embeddings/
    │   ├── figures/
    │   ├── logs/
    │   └── metrics/
    ├── scripts/
    ├── slurm/
    └── src/
```

Archivos clave:

| Ruta | Función |
|---|---|
| `scripts/00_verify_env.py` | Verifica Python, PyTorch, CUDA, OpenCLIP y dependencias principales. |
| `scripts/01_prepare_flickr30k_from_hf.py` | Prepara un subconjunto de `Vishva007/Flickr-Dataset-1k`. El nombre se conserva por compatibilidad histórica. |
| `scripts/02_build_embeddings.py` | Genera embeddings normalizados de imágenes y captions. |
| `scripts/03_eval_retrieval.py` | Calcula métricas de recuperación cruzada. |
| `scripts/04_eval_zeroshot.py` | Ejecuta una evaluación zero-shot simple sobre el bootstrap. |
| `scripts/05_mine_hard_negatives.py` | Lista pares imagen-caption incorrectos con alta similitud. |
| `scripts/run_local_pipeline.sh` | Ejecuta el flujo local completo con el bootstrap. |
| `scripts/run_hf_flickr1k_pipeline.sh` | Ejecuta el flujo extendido con Flickr1k desde Hugging Face. |
| `src/dataset_utils.py` | Carga metadata y expande captions. |
| `src/metrics.py` | Implementa métricas de ranking. |
| `src/openclip_utils.py` | Carga modelo, preprocess y tokenizer. |

#### 4. Requisitos

Hardware recomendado:

* GPU NVIDIA con soporte CUDA,
* 8 GB de VRAM o más para `ViT-B-32`,
* CPU suficiente para pruebas pequeñas con el bootstrap.

Software recomendado:

* Docker Engine,
* NVIDIA Container Toolkit,
* Imagen Docker del curso MCC225,
* Repositorio MCC225 montado en `/workspace`.

Dependencias adicionales del proyecto:

```text
PyYAML==6.0.2
datasets>=3.6.0,<5
Pillow>=10
```

`requirements-extra.txt` complementa el entorno principal del contenedor. No reemplaza las dependencias base del curso.

#### 5. Apertura del proyecto desde el sistema anfitrión

Esta sección se ejecuta desde la terminal del sistema anfitrión, es decir, fuera del contenedor Docker.

Verificar que Docker está disponible:

```bash
docker --version
```

Verificar que la GPU es visible para Docker:

```bash
docker run --rm --gpus all nvidia/cuda:12.1.1-base-ubuntu22.04 nvidia-smi
```

Verificar el contenedor activo del curso:

```bash
docker ps
```

En este laboratorio se usa como nombre de referencia:

```text
mcc225_gpu_container
```

Si `docker ps` muestra otro nombre, usar el nombre real del contenedor en los comandos siguientes.

#### 6. Acceso al contenedor Docker

#### 6.1 Entrar al contenedor con docker exec

Este comando se ejecuta desde el sistema anfitrión:

```bash
docker exec -it mcc225_gpu_container bash
```

Después de ejecutarlo, el prompt ya corresponde al entorno interno del contenedor.

#### 6.2 Confirmar que estás dentro del contenedor

Dentro del contenedor, verificar la ruta base:

```bash
pwd
```

La ruta esperada del repositorio es:

```text
/workspace
```

Verificar la GPU dentro del contenedor:

```bash
nvidia-smi
```

Verificar CUDA desde Python:

```bash
python - <<'PY'
import torch
print(torch.cuda.is_available())
print(torch.cuda.device_count())
PY
```

#### 6.3 Ubicarse en el proyecto

Los comandos del laboratorio se ejecutan dentro del contenedor, desde esta carpeta:

```bash
cd /workspace/Semana4/Proyecto
```

Verificar que estás en la carpeta correcta:

```bash
pwd
ls
```

La salida de `pwd` debe ser:

```text
/workspace/Semana4/Proyecto
```

#### 7. Preparación del entorno dentro del contenedor

Los siguientes comandos se ejecutan dentro del contenedor, después de entrar con `docker exec`.

Instalar dependencias adicionales:

```bash
pip install -r requirements-extra.txt
```

Instalar el proyecto en modo editable:

```bash
pip install -e .
```

Verificar que el paquete local carga correctamente:

```bash
python - <<'PY'
import src
print(src.__file__)
PY
```

La salida esperada debe apuntar a:

```text
/workspace/Semana4/Proyecto/src/__init__.py
```

Verificar el entorno:

```bash
python scripts/00_verify_env.py
```

#### 8. Ejecución rápida con el bootstrap local

Este flujo no requiere descargar datos desde Hugging Face. Usa el subconjunto incluido en:

```text
data/bootstrap_flickr30k/
```

Ejecutar dentro del contenedor:

```bash
bash scripts/run_local_pipeline.sh
```

El pipeline realiza:

1. verificación del entorno,
2. construcción de embeddings,
3. evaluación de recuperación cruzada,
4. minería de negativos duros,
5. evaluación zero-shot simple.

Salidas esperadas:

```text
outputs/embeddings/bootstrap_embeddings.npz
outputs/embeddings/bootstrap_embeddings.text_metadata.csv
outputs/metrics/retrieval_metrics.json
outputs/metrics/hard_negatives.csv
outputs/metrics/zeroshot_predictions.csv
```

Este es el flujo recomendado para una primera validación del contenedor.

#### 9. Ejecución extendida con Flickr1k

Este flujo usa Hugging Face y requiere conexión a internet dentro del contenedor.

Dataset remoto:

```text
Vishva007/Flickr-Dataset-1k
```

Ejecutar:

```bash
bash scripts/run_hf_flickr1k_pipeline.sh
```

Salidas esperadas:

```text
data/processed/flickr1k_hf/all.csv
data/processed/flickr1k_hf/train.csv
data/processed/flickr1k_hf/val.csv
data/processed/flickr1k_hf/test.csv
outputs/embeddings/flickr1k_embeddings.npz
outputs/embeddings/flickr1k_embeddings.text_metadata.csv
outputs/metrics/flickr1k_retrieval_metrics.json
outputs/metrics/flickr1k_hard_negatives.csv
```

El script acepta `Vishva007/Flickr-Dataset-1` y lo normaliza a `Vishva007/Flickr-Dataset-1k`.

#### 10. Ejecución paso a paso dentro del contenedor

#### 10.1 Preparar Flickr1k

```bash
python scripts/01_prepare_flickr30k_from_hf.py \
  --dataset-name Vishva007/Flickr-Dataset-1k \
  --hf-split train \
  --output-root data/processed/flickr1k_hf \
  --train-limit 512 \
  --val-limit 50 \
  --test-limit 50
```

#### 10.2 Construir embeddings

```bash
python scripts/02_build_embeddings.py \
  --metadata-csv data/processed/flickr1k_hf/all.csv \
  --model-name ViT-B-32 \
  --pretrained laion2b_s34b_b79k \
  --batch-size 32 \
  --caption-mode all \
  --output outputs/embeddings/flickr1k_embeddings.npz
```

#### 10.3 Evaluar recuperación cruzada

```bash
python scripts/03_eval_retrieval.py \
  --embeddings outputs/embeddings/flickr1k_embeddings.npz \
  --metadata-csv data/processed/flickr1k_hf/all.csv \
  --output-json outputs/metrics/flickr1k_retrieval_metrics.json \
  --hard-negatives-csv outputs/metrics/flickr1k_hard_negatives.csv \
  --top-n-hard-negatives 20
```

#### 10.4 Minar negativos duros

```bash
python scripts/05_mine_hard_negatives.py \
  --embeddings outputs/embeddings/flickr1k_embeddings.npz \
  --metadata-csv data/processed/flickr1k_hf/all.csv \
  --top-n 20
```

#### 11. Evaluación multi-caption

Los datasets tipo Flickr suelen tener varias captions válidas por imagen. Por eso el modo recomendado es:

```bash
--caption-mode all
```

Este modo considera positiva cualquier caption asociada al mismo `image_id`. Así se evita tratar como error una caption válida de la misma imagen.

Para una evaluación simplificada uno a uno se puede usar:

```bash
--caption-mode first
```

#### 12. Uso del cuaderno Jupyter

El notebook principal es:

```text
Cuaderno9-MCC225.ipynb
```

Abrir JupyterLab desde el entorno del curso y navegar a:

```text
/workspace/Semana4/Proyecto/Cuaderno9-MCC225.ipynb
```

Si se acaba de ejecutar `pip install -e .`, reiniciar el kernel antes de correr el cuaderno.

Recomendación:

```text
Kernel -> Restart Kernel and Run All Cells
```

#### 13. Métricas y resultados

Archivos de salida principales:

| Archivo | Contenido |
|---|---|
| `retrieval_metrics.json` | Métricas de recuperación cruzada. |
| `hard_negatives.csv` | Pares incorrectos con alta similitud. |
| `zeroshot_predictions.csv` | Predicciones zero-shot del bootstrap local. |
| `*.text_metadata.csv` | Relación entre embeddings textuales, captions e `image_id`. |

Métricas principales:

| Métrica | Interpretación |
|---|---|
| `R@1` | El positivo aparece en la primera posición. |
| `R@5` | El positivo aparece dentro de los cinco primeros resultados. |
| `R@10` | El positivo aparece dentro de los diez primeros resultados. |
| `MRR` | Promedio del inverso del ranking del primer positivo. |

#### 14. Actividad de laboratorio

#### 14.1 Parte A: smoke test local

Ejecutar:

```bash
bash scripts/run_local_pipeline.sh
```

Verificar que existan:

```text
outputs/metrics/retrieval_metrics.json
outputs/metrics/hard_negatives.csv
outputs/metrics/zeroshot_predictions.csv
```

Preguntas:

1. ¿Qué significa `R@1` en recuperación imagen a texto?
2. ¿Por qué `MRR` puede ser más informativo que accuracy en retrieval?
3. ¿Qué diferencia hay entre evaluar con una caption por imagen y evaluar con todas las captions?

#### 14.2 Parte B: Flickr1k

Ejecutar:

```bash
bash scripts/run_hf_flickr1k_pipeline.sh
```

Preguntas:

1. ¿Qué cambia en las métricas al usar `--caption-mode all`?
2. ¿Los hard negatives son errores claros o confusiones semánticamente razonables?
3. ¿Qué patrones de confusión aparecen en escenas con personas, objetos o actividades similares?

#### 14.3 Parte C: análisis de error

Abrir:

```text
outputs/metrics/flickr1k_hard_negatives.csv
```

Seleccionar cinco casos y completar:

| Caso | Caption verdadera | Caption negativa | Por qué el modelo la confundió | Qué evidencia visual falta |
|---|---|---|---|---|
| 1 | | | | |
| 2 | | | | |
| 3 | | | | |
| 4 | | | | |
| 5 | | | | |

#### 15. Entregables sugeridos

El estudiante debe entregar un informe breve en PDF, notebook exportado o documento indicado por el docente. No se debe crear un archivo Markdown adicional dentro del proyecto.

El informe debe incluir:

1. comandos ejecutados dentro del contenedor Docker,
2. evidencia de ejecución del pipeline local con el bootstrap,
3. evidencia de ejecución del pipeline remoto con `Vishva007/Flickr-Dataset-1k`, si hubo conexión a internet,
4. tabla comparativa con `R@1`, `R@5`, `R@10` y `MRR`,
5. análisis comentado de cinco hard negatives,
6. comparación entre `--caption-mode first` y `--caption-mode all`,
7. una mini ablación experimental,
8. conclusiones técnicas y limitaciones del modelo.

#### 15.1 Mini ablación sugerida

Realizar al menos una de las siguientes variaciones:

1. Cambiar el modo de captions.

```bash
--caption-mode first
```

```bash
--caption-mode all
```

2. Cambiar el tamaño de batch.

```bash
--batch-size 16
```

```bash
--batch-size 32
```

3. Comparar dos checkpoints de OpenCLIP.

```bash
--model-name ViT-B-32
--pretrained laion2b_s34b_b79k
```

```bash
--model-name RN50
--pretrained openai
```

#### 15.2 Preguntas para el informe

Responder brevemente:

1. ¿Qué cambia entre evaluar con una sola caption y evaluar con todas las captions asociadas a la misma imagen?
2. ¿Qué tipo de errores aparecen en los hard negatives?
3. ¿El modelo confunde objetos, acciones, contexto o relaciones espaciales?
4. ¿Qué checkpoint obtiene mejores métricas?
5. ¿Qué limitaciones tiene el bootstrap local frente a Flickr1k?
6. ¿Qué mejora concreta aplicarías en una siguiente versión del laboratorio?

#### 15.3 Formato de entrega

La entrega puede ser uno de estos formatos:

1. PDF breve,
2. notebook exportado a PDF,
3. documento externo indicado por el docente,
4. capturas y tablas pegadas en la plataforma del curso.

No crear archivos adicionales como:

```text
reports/semana4_resultados.md
LAB_SEMANA4.md
CHANGELOG_UNIFORMIZACION.md
```

Toda la documentación del proyecto debe mantenerse en este `README.md`.

#### 16. Flujo recomendado final

Desde el sistema anfitrión:

```bash
docker ps
docker exec -it mcc225_gpu_container bash
```

Dentro del contenedor:

```bash
cd /workspace/Semana4/Proyecto
pip install -r requirements-extra.txt
pip install -e .
python scripts/00_verify_env.py
bash scripts/run_local_pipeline.sh
bash scripts/run_hf_flickr1k_pipeline.sh
```

Para clase síncrona, usar primero el pipeline local. Para tarea o práctica extendida, usar Flickr1k.
