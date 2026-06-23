### Proyecto de la Semana 7: Patrimonio Andino Grounded

Esta carpeta contiene el proyecto `Patrimonio_Andino_Grounded`, utilizado como laboratorio aplicado de la **Semana 7** del curso **MCC225 - IA Generativa y Aprendizaje Multimodal**. El proyecto se apoya en el trabajo acumulado de las semanas previas sobre representación multimodal, fusión, aprendizaje contrastivo, recuperación cruzada y evaluación, y lo extiende hacia una tarea generativa controlada por evidencia.

El propósito de esta versión no es entrenar un modelo generativo grande desde cero, sino estudiar, ejecutar y discutir un flujo reproducible de:

1. **captioning factual**,
2. **generación condicionada por evidencia estructurada**,
3. **recuperación como soporte de grounding**,
4. **análisis visual-semántico con control de incertidumbre**,
5. **evaluación de salidas generativas en un dominio patrimonial**.

El caso de estudio se centra en objetos de patrimonio andino, principalmente registros de **Open Khipu** y **Paracas**, tratados como un corpus pequeño, curado y documentado.


#### 1. Ubicación esperada en el contenedor

Por compatibilidad con la estructura original del curso y con los notebooks ya preparados, la ruta recomendada sigue siendo:

```text
/workspace/Semana6/Proyecto/Patrimonio_Andino_Grounded/
```

En la Semana 7, el proyecto debe entenderse como un **proyecto puente**: fue preparado en la Semana 6, pero se usa de forma principal para el laboratorio de **captioning, generación condicionada y atención visual-semántica**.

La jerarquía esperada es:

```text
MCC225/
└── Semana6/
    └── Proyecto/
        └── Patrimonio_Andino_Grounded/
            ├── notebooks/
            ├── src/
            ├── configs/
            ├── data_raw/
            ├── data_interim/
            ├── data_processed/
            ├── outputs/
            └── docs/
```

Si se decide mover el proyecto físicamente a `Semana7/Proyecto/`, se debe revisar y actualizar cualquier referencia de ruta en:

```text
configs/docker_linux.yaml
README_local.md
docs/*.md
notebooks/*.ipynb
```

Para trabajo docente y reproducibilidad, se recomienda conservar la ruta original y documentar su uso como laboratorio de Semana 7.

#### 2. Primer notebook sugerido

El primer notebook que debe ejecutarse es:

```text
Patrimonio_Andino_Grounded/notebooks/10_verificacion_entorno_docker_linux.ipynb
```

Este cuaderno verifica que el entorno Docker/Linux esté correctamente configurado, que la raíz del proyecto sea detectable y que los archivos principales existan.

Después de esa verificación, la secuencia recomendada para la Semana 7 es:

```text
10_verificacion_entorno_docker_linux.ipynb
03_recuperacion_base_e_indices.ipynb
04_generacion_grounded.ipynb
05_evaluacion_y_ablaciones.ipynb
06_casos_curatoriales_y_exportacion.ipynb
07_demo_integrada_y_modelo_real_opcional.ipynb
09_casos_comentados_en_profundidad.ipynb
```

La secuencia completa de construcción del corpus, útil si se desea auditar todo el flujo desde los datos crudos, es:

```text
00_ingesta_open_khipu.ipynb
01_ingesta_paracas.ipynb
02_normalizacion_y_esquema.ipynb
03_recuperacion_base_e_indices.ipynb
04_generacion_grounded.ipynb
05_evaluacion_y_ablaciones.ipynb
06_casos_curatoriales_y_exportacion.ipynb
```

#### 3. Propósito académico de la Semana 7

En la Semana 7, el proyecto se usa para estudiar cómo una arquitectura multimodal aplicada puede pasar de la recuperación y la comparación a la **generación controlada**.

La pregunta central es:

> ¿Cómo generar descripciones y notas interpretativas sobre objetos patrimoniales sin inventar atributos no observados, manteniendo trazabilidad entre datos, recuperación, contexto y salida textual?

Desde una perspectiva de posgrado, el objetivo no es solo ejecutar notebooks. El objetivo es justificar metodológicamente:

- qué evidencia se usa,
- qué evidencia se descarta,
- qué se puede afirmar,
- qué se debe mantener como incertidumbre,
- qué errores son esperables,
- qué significa evaluar una salida generativa cuando el corpus es pequeño y especializado.


#### 4. Qué incluye el proyecto

El proyecto incluye:

- metadatos reales pequeños y curados,
- registros normalizados de Open Khipu y Paracas,
- un esquema unificado de atributos estructurales, textuales y contextuales,
- un recuperador textual basado en TF-IDF y similitud coseno,
- generación grounded mediante plantillas condicionadas por evidencia,
- salidas de captioning factual,
- notas técnico-curatoriales,
- notas comparativas basadas en vecinos recuperados,
- análisis de incertidumbre,
- métricas internas de cobertura, soporte y alucinación proxy,
- casos comentados para discusión académica,
- una ruta opcional para modelos reales de captioning y codificación imagen-texto.


#### 5. Qué no hace esta versión

Esta versión no debe interpretarse como un benchmark visual completo.

En particular:

- no redistribuye imágenes patrimoniales externas,
- no entrena modelos generativos grandes desde cero,
- no garantiza evaluación estadística robusta por tamaño de muestra,
- no sustituye el juicio experto curatorial,
- no convierte automáticamente metadatos en verdad visual,
- no debe usar recuperación como prueba de identidad cultural, cronológica o funcional.

El proyecto está diseñado para enseñar **disciplina generativa**: producir texto útil sin sobrepasar la evidencia disponible.


#### 6. Arranque rápido

Desde el contenedor del curso:

```bash
cd /workspace/Semana6/Proyecto/Patrimonio_Andino_Grounded
```

Verificar estructura:

```bash
python scripts/verificar_estructura_mcc225.py
```

Instalar dependencias, si el entorno base no las trae instaladas:

```bash
pip install -r requirements.txt
```

Abrir JupyterLab:

```bash
jupyter lab --ip=0.0.0.0 --port=8899 --allow-root
```

Luego abrir:

```text
http://localhost:8899/lab
```

y ejecutar primero:

```text
notebooks/10_verificacion_entorno_docker_linux.ipynb
```


#### 7 Atención visual-semántica

En esta versión, la atención visual-semántica se trabaja en dos niveles.

Primero, como **atención semántica guiada por evidencia**: el sistema selecciona qué campos del objeto, qué vecinos recuperados y qué atributos contextuales deben influir en la salida generada.

Segundo, como **ruta visual opcional**: si se agregan imágenes locales o URLs válidas en el manifiesto, el proyecto puede conectarse con modelos reales de captioning o codificación imagen-texto indicados en:

```text
configs/modelos_reales_opcionales.yaml
```

La atención visual-semántica debe discutirse con cuidado. Si no hay imagen local disponible, no se deben afirmar rasgos visuales no observados. En ese caso, el sistema debe declarar que trabaja con metadatos, estructura y contexto, no con inspección visual directa.

#### 8.  Evaluación y ablaciones

Ejecutar:

```text
notebooks/05_evaluacion_y_ablaciones.ipynb
```

Las métricas internas están en:

```text
src/metrics.py
```

El proyecto calcula:

- `attribute_coverage`: cobertura de atributos explícitos en el texto generado,
- `retrieval_support`: presencia de soporte recuperado en la traza;
- `hallucination_proxy`: penalización por expresiones de certeza indebida.

Las salidas principales se encuentran en:

```text
outputs/evaluacion/metricas_resumen.csv
outputs/evaluacion/resultados_por_registro.csv
outputs/evaluacion/analisis_error.csv
```

Estas métricas son operativas y deben leerse críticamente. No sustituyen métricas estándar de captioning, recuperación ni evaluación humana experta.

#### 9. Casos curatoriales y discusión

Ejecutar:

```text
notebooks/06_casos_curatoriales_y_exportacion.ipynb
notebooks/09_casos_comentados_en_profundidad.ipynb
```

Estos notebooks permiten pasar de la ejecución técnica a la interpretación académica. El estudiante debe revisar:

- si la salida mantiene fidelidad a los metadatos,
- si declara incertidumbre,
- si la comparación con vecinos recuperados está correctamente limitada,
- si la salida evita afirmar procedencia, cronología, función o significado sin evidencia suficiente,
- si el lenguaje es apropiado para documentación patrimonial.


#### 8. Estructura de datos usada por el proyecto

El proyecto trabaja con un esquema unificado donde cada registro puede contener:

```text
record_id
canonical_id
source
modality_type
title
description
object_type
culture
date_display
medium
provenance
institution
collection
rights
language
tags
image_path
image_url
split
x_s
x_t
x_c
qa_flags
```

La distinción conceptual más importante es:

- `x_s`: estructura del objeto o de la señal,
- `x_t`: descripción textual y palabras clave,
- `x_c`: contexto cultural, institucional o documental.

Esta separación permite discutir fusión multimodal y generación condicionada de forma explícita.


#### 9. Salidas esperadas

Después de ejecutar la ruta recomendada, el estudiante debería encontrar salidas en:

```text
outputs/captions/
outputs/notas_curatoriales/
outputs/comparativas/
outputs/evaluacion/
outputs/figuras/
docs/casos_comentados/
```

Archivos relevantes para revisión:

```text
outputs/evaluacion/metricas_resumen.csv
outputs/evaluacion/resultados_por_registro.csv
outputs/evaluacion/analisis_error.csv
outputs/evaluacion/casos_curatoriales.md
docs/casos_comentados/resumen_casos.md
```

La entrega mínima para la Semana 7 debe incluir:

1. ejecución reproducible de los notebooks principales,
2. un caption factual por registro seleccionado,
3. una nota técnico-curatorial generada bajo restricciones,
4. análisis de al menos dos casos,
5. discusión de una alucinación evitada o de un riesgo de alucinación,
6. interpretación crítica de las métricas internas,
7. explicación de cómo la recuperación condiciona la generación.

#### 10. Ruta opcional con modelos reales

El proyecto incluye una configuración opcional para modelos reales:

```text
configs/modelos_reales_opcionales.yaml
```

Modelos declarados:

```text
captioning_model: Salesforce/blip-image-captioning-base
text_encoder_model: sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2
image_encoder_model: openai/clip-vit-base-patch32
diffusion_model: stabilityai/stable-diffusion-xl-base-1.0
```

La ruta opcional se explora principalmente con:

```text
notebooks/07_demo_integrada_y_modelo_real_opcional.ipynb
notebooks/08_corrida_local_rtx4080_opcional.ipynb
```

Para usar imágenes locales, se debe:

1. agregar rutas o URLs al manifiesto correspondiente,
2. poblar `image_path` o `image_url`,
3. verificar permisos de uso,
4. ejecutar la descarga o vinculación de activos si corresponde,
5. separar claramente resultados basados en imagen real de resultados basados solo en metadatos.

#### 11. Relación con las semanas anteriores

##### Semana 2: modelos tempranos de alineamiento visual-semántico

La Semana 2 introduce la idea de que imágenes y textos pueden representarse en espacios relacionados. En este proyecto, esa idea aparece como antecedente conceptual: los objetos patrimoniales se describen mediante representaciones textuales, estructurales y contextuales que luego se alinean operativamente para recuperación y generación.

Aunque esta versión no depende obligatoriamente de imágenes reales, conserva la pregunta central del alineamiento visual-semántico: cómo vincular una entidad visual o material con una descripción textual controlada.

##### Semana 3: fusión multimodal

La Semana 3 estudia fusión temprana, intermedia y tardía. En este proyecto, esa discusión se observa en el diseño del esquema:

```text
x_s + x_t + x_c
```

La generación no usa un único campo plano. Combina estructura, texto y contexto de manera explícita. Esta combinación puede interpretarse como una forma didáctica de fusión intermedia/tardía, porque los atributos se mantienen separados durante la construcción de evidencia y se integran al momento de generar la salida.

##### Semana 4: aprendizaje contrastivo y recuperación cruzada

La Semana 4 trabaja el emparejamiento entre modalidades y los fundamentos de recuperación cruzada. En este proyecto, la recuperación no se usa solo como tarea final, sino como soporte para generación grounded.

La idea central heredada es:

> antes de generar, recuperar evidencia pertinente.

En los proyectos contrastivos, las consultas imagen-texto se resuelven mediante similitud en un espacio común. En `Patrimonio_Andino_Grounded`, el recuperador textual cumple una función análoga a escala reducida: identifica vecinos semánticamente próximos que ayudan a construir una nota comparativa, siempre con advertencias sobre la no equivalencia entre similitud y prueba histórica.

##### Semana 5: zero-shot, recuperación imagen-texto y métricas

La Semana 5 incorpora clasificación zero-shot, recuperación imagen-texto, prompt ensembles, comparación de checkpoints y métricas de ranking. Este proyecto retoma tres ideas:

1. las salidas dependen de cómo se formula la consulta o el prompt,
2. la recuperación debe evaluarse, no solo mostrarse,
3. los resultados deben acompañarse de análisis comparativo y límites.

La generación condicionada de Semana 7 puede entenderse como una extensión natural del prompting de Semana 5: el prompt deja de ser solo una plantilla de clasificación y se convierte en un contrato de evidencia que regula qué puede afirmar el sistema.

##### Semana 7: captioning, generación condicionada y atención visual-semántica

La Semana 7 consolida la progresión previa. El estudiante ya no solo recupera o clasifica, ahora debe generar texto con restricciones.

La contribución central del proyecto en esta semana es mostrar que un sistema generativo multimodal serio debe:

- conocer sus fuentes,
- declarar incertidumbre,
- separar evidencia de inferencia,
- evitar alucinaciones,
- evaluar sus salidas,
- documentar errores,
- permitir reproducción,
- explicar cómo los componentes de recuperación y representación influyen en la generación.


#### 12. Recomendación final 

Al trabajar este proyecto, no basta con ejecutar todos los notebooks. La pregunta de fondo es metodológica:

> ¿Qué condiciones mínimas debe cumplir una salida generativa para ser aceptable en un dominio patrimonial donde la evidencia es parcial, heterogénea y culturalmente sensible?.

