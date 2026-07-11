### Reporte individual de evaluación multimodal

#### Datos del estudiante

Nombre:
Repositorio:
Commit final:
Fecha:

#### Tarea definida

Explica qué sistema evaluastes, qué entrada recibe y qué salida produce.
Se evalua el aprendizaje constractivo con Openclip para el subconjunto de imágenes representativas de los deportes: 
"soccer",
"football",
"basketball",
"tennis",
"baseball",
"swimming",
"volleyball",
"golf",
"boxing",
"running",
"cycling",
"surfing",
"skiing"
Del msr-vtt
en el retrieval.
#### Dataset

Dataset MSR-VTT -116 videos de deportes seleccionados. 
número de imágenes: 116 (1 frame central por cada video), número de captions: 1 por video, filtros aplicados: Para la imagen borrosa se utiliza el filtro gausiano.

#### Modelos evaluados
Modelos: 
openai/clip-vit-base-patch32
Salesforce/blip-image-captioning-base

#### Baselines

Explica el baseline usado y por qué es una comparación mínima razonable.

#### Métricas

Reporte Recall@K, CLIPScore simplificado, métricas léxicas, resultados de CapFilt y resultados de ablación visual.

#### Análisis de errores

Incluye tabla de errores con categorías: objeto, acción, conteo, relación espacial, OCR, atributo, alucinación, sesgo, respuesta vaga y otro.

#### Discusión de limitaciones

Explica qué no capturan las métricas, dónde falla el modelo y qué supuestos pueden afectar la validez del experimento.

#### Conexión conceptual

Relaciona los resultados con BERT, VisualBERT, UNITER, ViLT, BLIP, BLIP-2 y LLaVA.

#### Conclusión

Resume si el sistema muestra alineamiento multimodal robusto o solo desempeño parcial.