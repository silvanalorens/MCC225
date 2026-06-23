# Integración con el contenedor Docker del curso

Esta versión asume que el curso se ejecuta dentro de un contenedor con el proyecto montado en `/workspace`.

## Decisiones de diseño

- todas las rutas se resuelven de forma relativa a la carpeta del proyecto;
- los notebooks evitan rutas absolutas dependientes del sistema operativo;
- la verificación inicial revisa Python, PyTorch, CUDA y la presencia del archivo `data_processed/records_master.jsonl`;
- la ruta opcional con GPU no reemplaza la lógica principal de recuperación y evidencia.

## Recomendación práctica

Si el proyecto queda en:

```text
/workspace/Semana6/Proyecto/Patrimonio_Andino_Grounded/
```

abre JupyterLab y ejecuta los notebooks desde `Patrimonio_Andino_Grounded/notebooks/`. Con eso, `Path("..")` apuntará a la raíz correcta del proyecto.
