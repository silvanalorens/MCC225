### Reporte individual de evaluación multimodal

#### Datos del estudiante

Nombre: Silvana Rosas Oquendo
Repositorio:: https://github.com/silvanalorens/MCC225/tree/main/Exposicion2
Commit final:
Fecha: 11/07/2026


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
Es una comparación mínima por tener un frame representativo.

#### Métricas

Reporte Recall@K, CLIPScore simplificado, métricas léxicas, resultados de CapFilt y resultados de ablación visual.

#### Análisis de errores

Se muestran errores de alucinación con relación al caption humano, debido a la extracción de único frame para un video. 

#### Discusión de limitaciones

Explica qué no capturan las métricas, dónde falla el modelo y qué supuestos pueden afectar la validez del experimento.
Blip fue más especifico, pero en algunos casos no brinda acción.
Se debe agregar más frames y generar más captions por cada uno. Mantener el caption general. 

#### Conexión conceptual

Relaciona los resultados con BERT, VisualBERT, UNITER, ViLT, BLIP, BLIP-2 y LLaVA.
prerequisito: Mayores frames por videos.
me parece que VisualBert sería más compatible por la representación visual de los frames. BLIP si es muy importante tener una fuente como video.
ViLT incluiría a futuro para ver su rendimiento.
#### Conclusión

Solo desempeño parcial, debí tener más frames para representar mejores momentos de videos
