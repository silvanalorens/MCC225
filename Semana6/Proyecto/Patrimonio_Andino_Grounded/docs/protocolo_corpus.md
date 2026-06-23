# Protocolo de corpus

## Unidad de registro
Cada línea del corpus procesado representa una unidad normalizada:
- un objeto,
- un objeto-vista,
- o una muestra analítica.

## Regla clave
No mezclar en un mismo registro una fotografía patrimonial y una imagen técnica de análisis si cumplen funciones distintas.

## Open Khipu
Open Khipu se trata aquí como corpus **estructural**:
- conteos de cordeles,
- grupos,
- colores,
- notas de procedencia,
- relaciones entre khipus.

## Paracas
Paracas se separa en dos ramas:
- `photo`
- `xrf_map`

## Calidad y faltantes
Los faltantes no se ocultan.
Se registran en `qa_flags` y se usan luego para:
- calibrar la generación,
- justificar incertidumbre,
- evitar sobreafirmaciones.

## Nota sobre esta versión
La carpeta incluye una muestra real pequeña curada desde metadatos públicos.
No redistribuye imágenes patrimoniales externas.
