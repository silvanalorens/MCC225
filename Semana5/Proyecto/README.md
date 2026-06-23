### **Semana 5: OpenCLIP para zero-shot y recuperación imagen-texto**

Este proyecto implementa un laboratorio reproducible de Semana 5 sobre **modelos contrastivos abiertos**, con énfasis en clasificación **zero-shot**, recuperación **imagen-texto**, recuperación **texto-imagen**, métricas de ranking, comparación de prompts y comparación de checkpoints de OpenCLIP.

> Este repositorio está pensado para ejecutarse con Docker y GPU NVIDIA. No requiere Kubernetes, Minikube ni `kubectl`.


#### **1. Propósito académico**

La Semana 5 del curso trabaja clasificación zero-shot, recuperación imagen-texto, métricas de evaluación, análisis comparativo y un laboratorio reproducible con un modelo contrastivo abierto. Este proyecto cubre ese objetivo mediante un flujo completo con OpenCLIP:

1. preparación de un subconjunto de evaluación de entre 100 y 500 imágenes cuando el entorno lo permita,
2. uso de un subconjunto bootstrap etiquetado para demostraciones controladas,
3. codificación de imágenes y textos en un espacio común,
4. evaluación de recuperación image-to-text y text-to-image,
5. evaluación zero-shot con plantillas de prompts cuando existan etiquetas compatibles,
6. comparación entre prompt único y prompt ensemble,
7. comparación de checkpoints abiertos,
8. construcción opcional de un índice FAISS para búsqueda semántica,
9. ruta opcional de fine-tuning corto con CSV.

El objetivo no es maximizar desempeño en un benchmark grande, sino mostrar de forma controlada y verificable cómo se diseña, ejecuta, evalúa y discute un pipeline contrastivo multimodal. Las métricas deben interpretarse de acuerdo con el tamaño y la naturaleza del subconjunto utilizado.

#### **2. Alcance del laboratorio**

**Incluido**

- Notebook principal: `Cuaderno10-MCC225.ipynb`.
- Scripts modulares en `scripts/`.
- Código reutilizable en `src/`.
- Configuraciones en `configs/`.
- Dataset bootstrap pequeño en `data/bootstrap_flickr30k/`.
- Preparación opcional de un subconjunto ampliado tipo Flickr de 100 a 500 imágenes.
- Métricas generadas en `outputs/metrics/`.
- Visualizaciones top-k y matriz de confusión para zero-shot cuando corresponda.
- Plantillas para Docker, Docker Compose, ejecución local, `torchrun` y SLURM.

**No incluido como objetivo principal**

- Entrenamiento serio a gran escala.
- Evaluación estadísticamente concluyente con el subconjunto bootstrap.
- Despliegue productivo.
- Uso de Kubernetes.
- Fine-tuning profundo de modelos fundacionales.

El fine-tuning incluido debe tratarse como una extensión operativa, no como el núcleo obligatorio del laboratorio.

#### **3. Estructura del proyecto**

```text
Proyecto/
├── Cuaderno10-MCC225.ipynb          # Notebook guiado del laboratorio
├── README.md                        # Documento principal del proyecto
├── docker-compose.yml               # Ejecución con Docker Compose y GPU
├── requirements-extra.txt           # Dependencias adicionales
├── configs/                         # Configuraciones de modelos, prompts y ejecución
├── data/bootstrap_flickr30k/        # Subconjunto pequeño con imágenes, captions, labels y queries
├── outputs/embeddings/              # Embeddings generados por OpenCLIP
├── outputs/metrics/                 # Resultados tabulares y métricas generadas
├── outputs/faiss/                   # Resultados de búsqueda semántica con FAISS, si se ejecuta
├── reports/                         # Reporte interpretativo generado o completado por el estudiante
├── scripts/                         # Scripts de ejecución, evaluación y entrenamiento
├── slurm/                           # Plantillas de referencia para HPC
└── src/                             # Funciones reutilizables del pipeline
```

Archivos clave:

| Ruta | Función |
|---|---|
| `scripts/00_verify_env.py` | Verifica Python, PyTorch, CUDA, OpenCLIP, FAISS y dependencias principales. |
| `scripts/02_build_embeddings.py` | Genera embeddings normalizados de imágenes y captions con OpenCLIP. |
| `scripts/03_eval_retrieval_metrics.py` | Calcula métricas de ranking para image-to-text y text-to-image. |
| `scripts/04_eval_zeroshot_prompt_ensembles.py` | Evalúa clasificación zero-shot con plantillas y ensemble de prompts. |
| `scripts/05_compare_checkpoints.py` | Compara checkpoints abiertos de OpenCLIP. |
| `scripts/06_build_faiss_index.py` | Construye búsqueda semántica con FAISS. |
| `scripts/07_validate_openclip_csv.py` | Valida el CSV antes de usarlo para fine-tuning. |
| `scripts/run_local_pipeline.sh` | Ejecuta el flujo completo de evaluación desde terminal. |
| `scripts/90_openclip_finetune_csv_single_gpu.sh` | Ejecuta un fine-tuning corto en una GPU. |


#### **4. Requisitos**

**Hardware recomendado**

- GPU NVIDIA con soporte CUDA.
- 8 GB de VRAM o más para la ejecución básica con `ViT-B-32`.
- Más VRAM si se usan checkpoints grandes como `ViT-L-14`.

**Software recomendado**

- Linux o entorno compatible con Docker.
- Docker Engine.
- NVIDIA Container Toolkit.
- Imagen base del curso con PyTorch y CUDA, por defecto: `mcc225_gpu:latest`.

**Dependencias Python adicionales**

Están listadas en `requirements-extra.txt`:

```text
open_clip_torch
faiss-cpu
PyYAML
datasets
matplotlib
pandas
scikit-learn
tqdm
Pillow
braceexpand
webdataset
```

#### **5. Apertura del proyecto desde terminal**

Esta sección se ejecuta **desde la terminal del sistema anfitrión**, es decir, fuera del contenedor Docker.

Ubicarse en la carpeta raíz del proyecto:

```bash
cd /workspace/Semana5/Proyecto
```

Si el proyecto fue descargado en otra ubicación, entrar a esa ruta antes de ejecutar Docker:

```bash
cd Proyecto
```

Verificar que Docker está disponible:

```bash
docker --version
docker compose version
```

Verificar que la GPU es visible para Docker:

```bash
docker run --rm --gpus all nvidia/cuda:12.1.1-base-ubuntu22.04 nvidia-smi
```

Si el comando anterior muestra la GPU, el entorno está listo para iniciar el contenedor del curso.

#### **6. Ejecución con Docker y acceso al contenedor**

##### **6.1 Levantar el contenedor**

Desde la terminal del sistema anfitrión, en la raíz del proyecto:

```bash
docker compose up -d
```

Verificar el nombre del contenedor activo:

```bash
docker ps
```

En este laboratorio se asume como nombre de referencia:

```text
mcc225_gpu_container
```

Si en `docker ps` aparece otro nombre, usar el nombre real del contenedor.

##### **6.2 Entrar al contenedor desde terminal**

Para abrir una shell interactiva dentro del contenedor:

```bash
docker exec -it mcc225_gpu_container bash
```

Este comando se ejecuta desde la terminal del sistema anfitrión. Después de ejecutarlo, el prompt ya corresponde al entorno interno del contenedor.

##### **6.3 Alternativa con Docker Compose**

Si se prefiere crear una sesión interactiva temporal mediante Docker Compose:

```bash
docker compose run --rm openclip bash
```

Esta alternativa es útil para pruebas puntuales, pero para trabajar sobre un contenedor ya levantado se recomienda usar:

```bash
docker exec -it mcc225_gpu_container bash
```

##### **6.4 Verificar GPU dentro del contenedor**

Una vez dentro del contenedor:

```bash
nvidia-smi
```

Si `nvidia-smi` muestra la GPU, se puede continuar con la instalación de dependencias y la ejecución del laboratorio.


#### **7. Preparación del entorno dentro del contenedor**

Los siguientes comandos se ejecutan **dentro del contenedor**, después de entrar con `docker exec` o con `docker compose run`.

Ubicarse en el proyecto:

```bash
cd /workspace/Semana5/Proyecto
```

Si el proyecto fue montado directamente como `/workspace/Proyecto`, usar:

```bash
cd /workspace/Proyecto
```

Instalar dependencias adicionales:

```bash
pip install -r requirements-extra.txt
```

Activar variables del proyecto:

```bash
source scripts/activate_project_env.sh
```

Verificar entorno:

```bash
python scripts/00_verify_env.py
```

Validar el CSV bootstrap de imágenes y captions:

```bash
python scripts/07_validate_openclip_csv.py --csv data/bootstrap_flickr30k/metadata.csv
```

Ejecutar el flujo completo desde terminal:

```bash
bash scripts/run_local_pipeline.sh
```

El flujo completo genera embeddings, métricas de recuperación, evaluación zero-shot, comparación de checkpoints y, cuando esté configurado, resultados FAISS.


#### **8. Uso del cuaderno Jupyter**

El notebook principal es:

```text
Cuaderno10-MCC225.ipynb
```

Este cuaderno puede ejecutarse desde JupyterLab, VS Code o un servidor Jupyter disponible dentro del contenedor.

Si se abre desde terminal dentro del contenedor, iniciar JupyterLab así:

```bash
cd /workspace/Semana5/Proyecto
jupyter lab --ip=0.0.0.0 --port=8888 --allow-root
```

Luego abrir en el navegador la URL que imprima JupyterLab, normalmente con el token de acceso.

Si se usa VS Code, abrir la carpeta del proyecto y seleccionar el kernel Python del contenedor.

Recomendación para evitar estados antiguos de memoria:

```text
Kernel -> Restart Kernel and Run All Cells
```

El cuaderno corregido realiza las siguientes validaciones metodológicas:

- verifica la correspondencia entre metadata, captions y embeddings;
- evita reutilizar embeddings incompatibles con la metadata activa;
- registra entorno, GPU, CUDA, PyTorch, OpenCLIP, fecha, modelo y checkpoint;
- limpia valores vacíos en tablas y figuras para no mostrar `NaN` como resultado docente;
- separa recuperación, zero-shot, FAISS, comparación de checkpoints y fine-tuning opcional;
- declara la evaluación zero-shot como demostrativa cuando el subconjunto ampliado no contiene etiquetas cerradas compatibles.


#### **9. Ejecución paso a paso desde terminal**

Los siguientes comandos se ejecutan dentro del contenedor, desde la raíz del proyecto.

##### **9.1 Generar embeddings**

```bash
python scripts/02_build_embeddings.py \
  --metadata-csv data/bootstrap_flickr30k/metadata.csv \
  --model-name ViT-B-32 \
  --pretrained laion2b_s34b_b79k \
  --output outputs/embeddings/bootstrap_embeddings.npz
```

##### **9.2 Evaluar recuperación imagen-texto y texto-imagen**

```bash
python scripts/03_eval_retrieval_metrics.py \
  --embeddings outputs/embeddings/bootstrap_embeddings.npz \
  --metadata-csv data/bootstrap_flickr30k/metadata.csv
```

Salidas esperadas:

```text
outputs/metrics/retrieval_metrics.json
outputs/metrics/retrieval_per_query.csv
outputs/metrics/hard_negatives.csv
```

##### **9.3 Evaluar zero-shot con prompts**

```bash
python scripts/04_eval_zeroshot_prompt_ensembles.py \
  --embeddings outputs/embeddings/bootstrap_embeddings.npz \
  --metadata-csv data/bootstrap_flickr30k/metadata.csv \
  --prompt-config data/bootstrap_flickr30k/prompt_config.json
```

Salidas esperadas:

```text
outputs/metrics/zeroshot_prompt_summary.csv
outputs/metrics/zeroshot_predictions.csv
outputs/metrics/zeroshot_confusion.csv
```

##### **9.4 Comparar checkpoints**

```bash
python scripts/05_compare_checkpoints.py \
  --metadata-csv data/bootstrap_flickr30k/metadata.csv \
  --checkpoint-config configs/checkpoints.yaml \
  --prompt-config data/bootstrap_flickr30k/prompt_config.json
```

Salida esperada:

```text
outputs/metrics/checkpoint_comparison.csv
```

##### **9.5 Construir índice FAISS**

```bash
python scripts/06_build_faiss_index.py \
  --embeddings outputs/embeddings/bootstrap_embeddings.npz \
  --metadata-csv data/bootstrap_flickr30k/metadata.csv \
  --queries-csv data/bootstrap_flickr30k/queries.csv
```

Salida esperada:

```text
outputs/faiss/query_results.csv
```


#### **10. Resultados incluidos como referencia**

El proyecto trae resultados generados sobre un subconjunto bootstrap pequeño:

| Evaluación | Resultado observado |
|---|---:|
| Número de imágenes | 6 |
| Número de captions | 30 |
| Image-to-text R@1 | 1.0000 |
| Image-to-text MRR | 1.0000 |
| Text-to-image R@1 | 0.9333 |
| Text-to-image MRR | 0.9667 |
| Zero-shot prompt ensemble accuracy | 0.8333 |

En la evaluación zero-shot incluida, el caso fallido corresponde a una imagen `people_outdoors` clasificada como `maintenance`. Esta confusión es didácticamente útil porque permite discutir ambigüedad visual, sensibilidad a prompts y diferencia entre recuperación por captions y clasificación por etiquetas.

Comparación de checkpoints incluida:

| Checkpoint | I2T R@1 | T2I R@1 | Zero-shot ensemble accuracy |
|---|---:|---:|---:|
| `ViT-B-32 / laion2b_s34b_b79k` | 1.0000 | 0.9333 | 0.8333 |
| `ViT-B-16 / datacomp_xl_s13b_b90k` | 1.0000 | 0.9333 | 1.0000 |
| `ViT-L-14 / openai` | 1.0000 | 0.9667 | 0.8333 |

Estos resultados no deben interpretarse como evidencia general de superioridad de un checkpoint. El tamaño del subconjunto bootstrap es deliberadamente pequeño y sirve para discusión metodológica, no para inferencia estadística robusta.

Cuando se usa el subconjunto ampliado, la recuperación imagen-texto y texto-imagen puede discutirse con mayor solidez descriptiva. Sin embargo, si dicho subconjunto no contiene etiquetas cerradas compatibles, la evaluación zero-shot debe reportarse como demostración docente sobre el bootstrap etiquetado.


#### **11. Ejercicios y extensiones opcionales**

##### **11.1 Ejercicios obligatorios sugeridos**

1. Preparar o justificar un subconjunto de evaluación de entre 100 y 500 imágenes.
2. Registrar entorno, GPU, CUDA, PyTorch, OpenCLIP, fecha, modelo y checkpoint.
3. Construir embeddings reproducibles y verificar su correspondencia con metadata y captions.
4. Evaluar recuperación imagen->texto y texto->imagen.
5. Visualizar resultados top-k y discutir aciertos, errores y ambigüedades.
6. Evaluar zero-shot solo cuando existan etiquetas compatibles; si no existen, declararlo como demostración docente.
7. Presentar matriz de confusión para zero-shot cuando corresponda.
8. Comparar checkpoints y documentar costo computacional cuando sea posible.
9. Ejecutar pruebas mínimas de `src/metrics.py`.
10. Entregar un reporte interpretativo con resultados, limitaciones y análisis de error.

##### **11.2 Extensiones opcionales**

- Construcción de índice FAISS para búsqueda eficiente.
- Medición exhaustiva de costo por checkpoint.
- Ejecución con `torchrun` o SLURM.
- Incorporación de nuevas consultas textuales.
- Fine-tuning corto de OpenCLIP.

El fine-tuning debe tratarse como **demostración operativa**, no como evidencia concluyente de mejora, salvo que exista separación entrenamiento/validación/prueba, control de semillas, comparación con línea base, análisis de sobreajuste y evaluación en datos no vistos.

#### **12. Fine-tuning opcional en una GPU**

Antes de entrenar, validar el CSV:

```bash
python scripts/07_validate_openclip_csv.py --csv data/bootstrap_flickr30k/metadata.csv
```

Ejecutar fine-tuning corto:

```bash
CUDA_VISIBLE_DEVICES=0 \
BATCH_SIZE=8 \
EPOCHS=1 \
WORKERS=2 \
PRECISION=amp \
bash scripts/90_openclip_finetune_csv_single_gpu.sh
```

Si aparece error de memoria CUDA, reducir el batch size:

```bash
CUDA_VISIBLE_DEVICES=0 \
BATCH_SIZE=4 \
EPOCHS=1 \
WORKERS=2 \
PRECISION=amp \
bash scripts/90_openclip_finetune_csv_single_gpu.sh
```

El resultado de este ajuste no debe reportarse como mejora concluyente sin una evaluación experimental rigurosa sobre datos no vistos.


#### **13. Limpieza de salidas generadas**

Para reconstruir resultados desde cero:

```bash
rm -rf outputs/embeddings/*
rm -rf outputs/metrics/*
rm -rf outputs/faiss/*
rm -rf reports/*.md
```

Para eliminar archivos temporales de Python y Jupyter:

```bash
find . -type d -name "__pycache__" -prune -exec rm -rf {} +
find . -type d -name ".ipynb_checkpoints" -prune -exec rm -rf {} +
find . -type f -name "*.pyc" -delete
```

#### **14. Nota metodológica final**

Este laboratorio debe evaluarse por la calidad del flujo metodológico: preparación de datos, trazabilidad del entorno, reproducibilidad de embeddings, pertinencia de métricas, visualización de resultados, análisis de error y reconocimiento explícito de limitaciones.

Las métricas obtenidas sobre subconjuntos pequeños son útiles para verificar el funcionamiento del pipeline, pero no constituyen evidencia estadística suficiente para afirmar superioridad general de un checkpoint, prompt o estrategia de entrenamiento.