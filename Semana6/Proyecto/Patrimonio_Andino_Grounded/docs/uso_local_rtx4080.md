# Uso local opcional con RTX 4080

## Cuándo conviene

Esta ruta sirve cuando el contenedor del curso se ejecuta en Linux con acceso a GPU y ya verificaste que `torch.cuda.is_available()` devuelve `True`.

## Orden recomendado

1. Ejecutar `notebooks/10_verificacion_entorno_docker_linux.ipynb`.
2. Ejecutar `notebooks/07_demo_integrada_y_modelo_real_opcional.ipynb`.
3. Ejecutar `notebooks/08_corrida_local_rtx4080_opcional.ipynb`.

## Alcance de la ruta opcional

- captioning real con un modelo abierto ligero;
- contraste entre salida del modelo y salida grounded del proyecto;
- pruebas pequeñas de generación condicionada, solo si el entorno y la memoria lo permiten.

## Precaución metodológica

La GPU mejora la experimentación, pero no sustituye la lógica de evidencia: recuperación, estructura y metadatos siguen siendo el núcleo del proyecto.
