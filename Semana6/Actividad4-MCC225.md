### Actividad 4-MCC225 

#### Captioning grounded, generación condicionada y atención visual-semántica

Esta actividad conecta directamente la secuencia de trabajo anterior del curso:

- **Semana 4:** aprendizaje contrastivo, embeddings imagen-texto, recuperación cruzada, métricas de ranking y análisis de negativos duros.
- **Semana 5:** clasificación zero-shot, recuperación imagen-texto/texto-imagen, comparación de prompts, checkpoints e índice FAISS.
- **Proyecto Patrimonio_Andino_Grounded:** recuperación + generación grounded sobre registros patrimoniales de Open Khipu y Paracas, con énfasis en trazabilidad de evidencia, generación condicionada, incertidumbre y evaluación de alucinación operativa.
- **Actividad 4 (esta entrega):** transformar la recuperación multimodal y los metadatos estructurados en un sistema de **descripción generativa controlada**, capaz de producir captions o notas técnico-curatoriales con evidencia explícita, comparar condiciones de generación y discutir cuándo existe soporte visual-semántico suficiente y cuándo solo existe grounding catalográfico.

La meta ya no es únicamente recuperar pares imagen-texto o clasificar zero-shot, sino **razonar críticamente sobre cómo una salida generativa debe estar condicionada por evidencia visual, textual, estructural y recuperada**. La actividad exige distinguir entre captioning visual clásico, generación condicionada por metadatos, generación aumentada por recuperación y generación grounded con trazabilidad.

#### Objetivos de aprendizaje

Al finalizar esta actividad, cada estudiante debería poder:

1. Explicar la transición conceptual desde **alineamiento contrastivo** y **recuperación cruzada** hacia **captioning grounded** y generación condicionada.
2. Comparar un pipeline dual-encoder de Semanas 4 y 5 con un pipeline de recuperación + generación del proyecto `Patrimonio_Andino_Grounded`.
3. Implementar o adaptar un flujo reproducible que genere descripciones breves, notas comparativas o notas técnico-curatoriales usando evidencia explícita.
4. Construir una representación mínima de **atención visual-semántica o atención sobre evidencia**, indicando qué atributos, vecinos recuperados o señales visuales soportan cada salida generada.
5. Evaluar las salidas generativas mediante métricas operativas, análisis de error, trazas de evidencia y revisión cualitativa.
6. Reconocer limitaciones metodológicas: ausencia de imagen redistribuible, dependencia de metadatos, ambigüedad curatorial, falsos soportes de recuperación y riesgo de alucinación.
7. Formular una ruta de mejora para convertir un prototipo descriptivo en un componente del trabajo integrador final.

#### Material obligatorio de referencia

La actividad debe apoyarse primordialmente en los siguientes materiales del curso:

- `Semana4/Proyecto/Cuaderno9-MCC225.ipynb`
- `Semana4/Proyecto/README.md`
- `Semana4/Proyecto/scripts/03_eval_retrieval.py`
- `Semana4/Proyecto/scripts/05_mine_hard_negatives.py`
- `Semana4/Proyecto/src/metrics.py`
- `Semana5/Proyecto/Cuaderno10-MCC225.ipynb`
- `Semana5/Proyecto/README.md`
- `Semana5/Proyecto/scripts/03_eval_retrieval_metrics.py`
- `Semana5/Proyecto/scripts/04_eval_zeroshot_prompt_ensembles.py`
- `Semana5/Proyecto/scripts/06_build_faiss_index.py`
- `Semana6/Proyecto/Patrimonio_Andino_Grounded/README_local.md`
- `Semana6/Proyecto/Patrimonio_Andino_Grounded/notebooks/03_recuperacion_base_e_indices.ipynb`
- `Semana6/Proyecto/Patrimonio_Andino_Grounded/notebooks/04_generacion_grounded.ipynb`
- `Semana6/Proyecto/Patrimonio_Andino_Grounded/notebooks/05_evaluacion_y_ablaciones.ipynb`
- `Semana6/Proyecto/Patrimonio_Andino_Grounded/notebooks/07_demo_integrada_y_modelo_real_opcional.ipynb`
- `Semana6/Proyecto/Patrimonio_Andino_Grounded/notebooks/09_casos_comentados_en_profundidad.ipynb`
- `Semana6/Proyecto/Patrimonio_Andino_Grounded/configs/prompts_es.yaml`
- `Semana6/Proyecto/Patrimonio_Andino_Grounded/data_processed/catalogo_objetos.csv`
- `Semana6/Proyecto/Patrimonio_Andino_Grounded/data_processed/catalogo_imagenes.csv`
- `Semana6/Proyecto/Patrimonio_Andino_Grounded/outputs/evaluacion/metricas_resumen.csv`
- `Semana6/Proyecto/Patrimonio_Andino_Grounded/outputs/evaluacion/resultados_por_registro.csv`

Si el estudiante dispone de GPU e imágenes válidas, puede usar la ruta opcional con modelo real de captioning. Si no dispone de imágenes redistribuibles o el registro aparece como `no_image`, deberá trabajar 
con **grounding catalográfico y estructural**, y explicitar esa condición en su análisis.

#### Instrucciones generales

Cada estudiante debe entregar **un notebook integrado y comentado**, construido a partir de los materiales de Semanas 4, 5 y del proyecto `Patrimonio_Andino_Grounded`. 
El notebook debe mostrar que el estudiante entiende la diferencia entre:

- recuperar vecinos semánticos,
- clasificar zero-shot,
- generar un caption factual (descripción basada en hechos),
- generar una nota condicionada por evidencia,
- producir una comparación curatorial,
- y justificar qué evidencia soporta o no soporta una afirmación generada.

No se exige entrenar un modelo grande ni reproducir por completo todos los pipelines de Semanas 4 y 5. Sí se exige demostrar, con código y análisis, que la generación de texto multimodal no debe evaluarse solo por fluidez, sino por **soporte, trazabilidad, control de inferencia y disciplina frente a la incertidumbre**.

#### Producto a entregar

Entregar **1 notebook Jupyter** con el nombre:

```text
ApellidoNombre-Actividad4-MCC225.ipynb
```

El notebook debe ejecutarse de principio a fin en el entorno del curso, usando rutas relativas o detección robusta de `PROJECT_ROOT`. Puede incluir una sección exploratoria opcional, pero se debe separar claramente lo obligatorio de lo experimental.

#### Estructura mínima obligatoria del notebook

##### 1. Título y contexto

Incluye:

- nombre de la actividad,
- nombre del estudiante,
- título breve del experimento,
- ruta local del proyecto usado,
- indicación explícita de si trabajó con imágenes reales, metadatos, estructura o una combinación.

En esta sección resume en **4 a 6 líneas** qué significa hacer captioning o generación condicionada en un dominio patrimonial donde no todos los registros tienen imagen disponible.

##### 2. Puente conceptual: de Semanas 4 y 5 a Semana 7

Construye una síntesis breve de la progresión:

| Etapa | Material de referencia | Pregunta central | Salida técnica | Límite para Semana 7 |
|---|---|---|---|---|
| Semana 4 | OpenCLIP, embeddings, retrieval | ¿Qué tan bien se alinean imagen y texto? | ranking, R@k, MRR, negativos díficiles | no genera explicación ni caption grounded |
| Semana 5 | zero-shot, prompts, FAISS | ¿Cómo clasificar o buscar sin entrenamiento supervisado directo? | predicción, top-k, índice semántico | la etiqueta no basta para describir evidencia |
| Proyecto Patrimonio | recuperación + generación grounded | ¿Cómo redactar texto controlado por evidencia? | caption, nota, comparación, traza | riesgo de grounding solo catalográfico |
| Semana 7 | captioning y generación condicionada | ¿Qué debe decir el sistema y con qué soporte? | descripción multimodal verificable | requiere evaluación de alucinación y soporte |

La tabla puede ampliarse, pero debe discutir explícitamente por qué una métrica de recuperación no garantiza una buena generación descriptiva.

##### 3. Diagnóstico del corpus Patrimonio_Andino_Grounded

Carga e inspecciona al menos estos archivos:

```text
data_processed/catalogo_objetos.csv
data_processed/catalogo_imagenes.csv
data_processed/resumen_splits.csv
outputs/evaluacion/metricas_resumen.csv
```

Debes reportar:

1. número de registros por `source`,
2. número de registros por `modality_type`,
3. distribución de `split`,
4. campos faltantes relevantes,
5. cuántos registros permiten captioning visual real y cuántos solo permiten generación basada en metadatos,
6. qué implicancias tiene esto para evaluar atención visual-semántica.

Incluye al menos **una tabla** y **una figura**. La figura puede ser un gráfico de barras de modalidades, splits o cobertura de campos.

##### 4. Recuperación como control de evidencia

Usa el flujo conceptual de Semanas 4 y 5 para analizar la recuperación dentro del proyecto patrimonial.

Como mínimo:

1. Selecciona **tres registros**:
   - un khipu de Open Khipu,
   - un objeto Paracas con `photo`,
   - el caso `xrf_map` o un registro marcado como challenge.
2. Para cada registro, recupera vecinos o inspecciona los vecinos ya generados en las salidas del proyecto.
3. Registra el top-k o la traza de vecinos.
4. Indica si los vecinos son útiles para:
   - describir atributos,
   - comparar materialidad,
   - inferir procedencia,
   - o únicamente sugerir afinidad débil.

Debes incluir una tabla con las columnas mínimas:

| Registro | Tipo de modalidad | Vecinos recuperados | Evidencia útil | Riesgo de sobreinterpretación | Decisión |
|---|---|---|---|---|---|

Conecta esta sección con los conceptos de **hard negatives** de Semana 4 y con la búsqueda semántica/FAISS de Semana 5. No basta con listar vecinos: debes interpretar si son evidencia fuerte, evidencia débil o distractores semánticos.

##### 5. Generación condicionada y comparación de prompts

Trabaja con los prompts del archivo:

```text
configs/prompts_es.yaml
```

Como mínimo debes comparar **dos condiciones de generación**:

- **Condición A:** caption factual breve usando solo metadatos directos.
- **Condición B:** nota técnico-curatorial usando metadatos + estructura + recuperación.

Opcionalmente puedes añadir:

- **Condición C:** nota comparativa con vecinos recuperados.
- **Condición D:** salida con modelo real de captioning si hay imagen y GPU disponible.

Para cada una de las tres piezas seleccionadas, genera o inspecciona:

1. `caption_factual`,
2. `nota_tecnico_curatorial`,
3. `nota_comparativa`,
4. `incertidumbre`,
5. `traza_evidencia`.

Incluye una tabla de comparación:

| Registro | Condición | Texto generado | Evidencia usada | Afirmación no soportada detectada | Corrección propuesta |
|---|---|---|---|---|---|

La evaluación principal no es si el texto "suena bien", sino si la salida mantiene disciplina inferencial: no debe inventar cronología, función, procedencia, simbolismo ni identidad histórica cuando la evidencia no lo permite.

##### 6. Atención visual-semántica o atención sobre evidencia

Debes implementar una pequeña función que aproxime una de estas dos opciones:

**Opción 1: atención visual-semántica real, si hay imágenes disponibles.**

Usa embeddings imagen-texto, similitud por prompts, mapas de activación o una estrategia equivalente para indicar qué partes de la imagen o qué descriptores visuales sostienen una frase generada. No se exige un método perfecto, pero sí una justificación metodológica clara.

**Opción 2: atención sobre evidencia, si no hay imágenes disponibles.**

Construye una función, por ejemplo:

```python
def evidence_attention(record, generated_text, neighbors=None):
    """
    Devuelve una tabla que indique qué campos del registro o vecinos recuperados
    soportan cada oración o fragmento del texto generado.
    """
```

La función debe producir una tabla con columnas como:

| Fragmento generado | Campo soporte | Tipo de soporte | Puntaje | Comentario |
|---|---|---|---|---|

Tipos de soporte sugeridos:

- `visual_directo`, si proviene de imagen disponible,
- `catalografico`, si proviene de metadatos,
- `estructural`, si proviene de atributos como cordeles, colores, grupos o material,
- `recuperado`, si proviene de vecinos,
- `no_soportado`, si no hay evidencia suficiente.

La salida debe visualizarse mediante una tabla coloreada, heatmap simple o gráfico de barras. Esta sección representa la parte de **atención visual-semántica** de la Semana 7: cuando no hay atención visual real, debes defender una atención sobre evidencia como sustituto metodológico explícito, no como equivalente pleno.

##### 7. Evaluación, ablaciones y análisis de error

Usa o adapta las métricas del proyecto:

- `attribute_coverage`,
- `retrieval_support`,
- `hallucination_proxy`,
- revisión manual de precisión factual,
- claridad de incertidumbre,
- utilidad descriptiva.

Realiza al menos **dos ablaciones**:

1. **Sin recuperación vs. con recuperación.**
2. **Prompt factual estricto vs. nota técnico-curatorial extendida.**

Opcionalmente:

3. `top_k=1` vs. `top_k=3` o `top_k=5`.
4. prompt único vs. plantilla de prompts.
5. modelo real de captioning vs. generación basada en metadatos.

Incluye una tabla comparativa:

| Ablación | Cobertura de atributos | Soporte de recuperación | Alucinación proxy | Juicio cualitativo | Decisión |
|---|---:|---:|---:|---|---|

Luego selecciona **tres errores o riesgos** y clasifícalos:

- error factual,
- inferencia excesiva,
- vecino recuperado engañoso,
- ausencia de soporte visual,
- ambigüedad catalográfica,
- prompt demasiado permisivo,
- métrica operativa insuficiente.

Para cada error, indica una corrección concreta.

##### 8. Mini componente implementado por el estudiante

Debes implementar una pieza propia de código. Puede ser una de las siguientes:

1. `evidence_attention(...)`, descrita arriba.
2. `grounding_audit(...)`, que marque afirmaciones soportadas/no soportadas.
3. `compare_generation_modes(...)`, que ejecute varias condiciones y resuma métricas.
4. `prompt_strictness_ablation(...)`, que compare prompts con distinto nivel de restricción.
5. `retrieval_to_generation_report(...)`, que convierta vecinos recuperados en una tabla de soporte para generación.

La función debe recibir entradas reales del proyecto y devolver un `DataFrame`, una figura o ambos. No se aceptará una función aislada sin conexión con los datos.

##### 9. Discusión metodológica 

Redacta una discusión de **600 a 900 palabras** que responda:

1. ¿En qué se diferencia un caption visual clásico de una nota grounded patrimonial?,
2. ¿Qué se gana y qué se pierde al usar recuperación como soporte de generación?,
3. ¿Cuándo un vecino recuperado debe tratarse como evidencia y cuándo solo como contexto?,
4. ¿Qué significa "atención visual-semántica" cuando parte del corpus no tiene imagen disponible?,
5. ¿Por qué métricas como cobertura de atributos o alucinación proxy son útiles pero insuficientes?,
6. ¿Qué diseño propondrías para escalar este prototipo a un dataset mayor?.

> Una **alucinación proxy** suele referirse a una respuesta o señal indirecta que parece indicar algo real sobre el mundo, pero en realidad es una inferencia falsa o engañosa del modelo. 

La discusión debe apoyarse en resultados observados, no solo en definiciones generales.

##### 10. Ruta propuesta para el trabajo integrador

Cierra con una propuesta de continuación que incluya:

1. tipo de sistema que se podría construir,
2. modalidad principal y modalidades auxiliares,
3. fuente de evidencia primaria,
4. modelo o familia de modelos a usar,
5. métrica principal,
6. análisis de error previsto,
7. riesgo de alucinación o falta de grounding,
8. experimento pequeño reproducible para la siguiente semana.

##### 11. Limitaciones, dudas y preguntas abiertas

Cierra con una sección breve donde respondas:

- ¿qué parte del pipeline quedó realmente grounded?,
- ¿qué parte depende solo de metadatos?,
- ¿qué afirmación sería irresponsable generar con la evidencia disponible?,
- ¿qué evidencia adicional necesitarías para mejorar el captioning?,
- ¿qué métrica agregarías si tuvieras evaluación humana experta?.

#### Requisitos mínimos de código

El notebook debe:

- ejecutarse de principio a fin sin depender de rutas locales privadas,
- usar `pandas`, `matplotlib` y al menos una función propia,
- cargar al menos tres archivos reales del proyecto patrimonial,
- incluir al menos una tabla comparativa y una figura,
- seleccionar al menos tres registros de análisis,
- comparar al menos dos condiciones de generación,
- realizar al menos dos ablaciones,
- incluir una tabla de soporte/evidencia por fragmento generado,
- discutir explícitamente si el soporte es visual, catalográfico, estructural o recuperado,
- separar resultados obligatorios de extensiones opcionales,
- registrar limitaciones del entorno, especialmente ausencia de GPU, ausencia de imagen o imposibilidad de ejecutar modelos reales.

#### Plantilla breve sugerida

```markdown
## Actividad 4-MCC225
### Captioning grounded, generación condicionada y atención visual-semántica

**Estudiante:**  
**Título del experimento:**  
**Ruta del proyecto usado:**  
**Modalidades disponibles:**  

#### 1. Título y contexto
#### 2. Puente conceptual: Semanas 4 y 5 hacia Semana 7
#### 3. Diagnóstico del corpus Patrimonio_Andino_Grounded
#### 4. Recuperación como control de evidencia
#### 5. Generación condicionada y comparación de prompts
#### 6. Atención visual-semántica o atención sobre evidencia
#### 7. Evaluación, ablaciones y análisis de error
#### 8. Mini componente implementado por el estudiante
#### 9. Discusión metodológica
#### 10. Ruta propuesta para el trabajo integrador
#### 11. Limitaciones, dudas y preguntas abiertas
```

#### Recomendación final

La meta de esta actividad no es producir textos largos ni estéticamente convincentes. La meta es aprender a responder una pregunta central de los sistemas generativos multimodales:

> **¿Qué puede afirmar responsablemente un sistema generativo sobre una imagen, objeto o registro patrimonial, y qué evidencia sostiene cada afirmación?**

Es preferible una generación breve, trazable y metodológicamente honesta que una descripción extensa, fluida y no verificable.
