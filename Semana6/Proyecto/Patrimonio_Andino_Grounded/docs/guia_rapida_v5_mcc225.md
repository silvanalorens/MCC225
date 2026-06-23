# Guía rápida v5 para MCC225

## Ruta esperada

```text
/workspace/Semana6/Proyecto/Patrimonio_Andino_Grounded/
```

## Secuencia corta

1. `10_verificacion_entorno_docker_linux.ipynb`
2. `07_demo_integrada_y_modelo_real_opcional.ipynb`
3. `08_corrida_local_rtx4080_opcional.ipynb` si hay GPU
4. `09_casos_comentados_en_profundidad.ipynb`

## Secuencia completa

`00` → `01` → `02` → `03` → `04` → `05` → `06`

## Qué revisar primero

- que `data_processed/records_master.jsonl` exista;
- que la raíz del proyecto se detecte correctamente;
- que `torch.cuda.is_available()` sea verdadero solo cuando estés en la imagen GPU.

## Recomendación práctica

Para clase, usa la ruta corta. Para adaptar o ampliar el proyecto, usa la secuencia completa `00–06`.
