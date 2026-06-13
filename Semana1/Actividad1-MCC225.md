## Actividad 1-MCC225

### Propuesta inicial de problema multimodal

##### Objetivo
Que cada estudiante proponga un posible **problema multimodal** para desarrollar durante el curso y lo clasifique según el tipo principal detarea: **clasificación**, **retrieval**, **VQA**, **generación** u otra categoría relacionada.

#### Instrucciones
Cada estudiante debe proponer **1 problema multimodal** original o adaptado a un contexto real.

La propuesta debe responder, como mínimo, a las siguientes preguntas:

1. **Nombre del problema**  
   Escribe un título breve y claro.

2. **Contexto o aplicación**  
   Explica en 3 a 5 líneas en qué situación real aparece el problema. Puede pertenecer a educación, salud, industria, seguridad, comercio, documentos, redes sociales, medios, etc.

4. **Modalidades involucradas**  
   Indica qué tipos de datos intervienen. Por ejemplo:
   - texto + imagen
   - texto + audio
   - video + texto
   - imagen + audio
   - documento escaneado + texto

5. **Entrada y salida esperada**  
   Describe qué recibe el sistema y qué debería producir.

6. **Tipo de tarea principal**  
   Señala si el problema corresponde principalmente a una de estas categorías:
   - **Clasificación**: asignar una categoría o etiqueta.
   - **Retrieval**: recuperar contenido relacionado entre modalidades.
   - **VQA**: responder preguntas sobre una imagen, video o documento visual.
   - **Generación**: producir texto, imagen, resumen, caption u otra salida generativa.
   - **Otra/mixta**: si combina varias tareas, indícalo y explica cuál domina.

7. **Por qué es multimodal**  
   Explica brevemente por qué no bastaría usar una sola modalidad.

8. **Posible dato o dataset**  
   Menciona de dónde podrían salir los datos: dataset público, datos propios, documentos, imágenes web, videos, audios, etc.

9. **Modelo o enfoque base posible**  
   Menciona una línea base tentativa. No tiene que ser definitiva. Por ejemplo:
   - CLIP/OpenCLIP
   - BLIP/BLIP-2
   - ViT + encoder de texto
   - Modelo VLM abierto
   - sistema con recuperación multimodal

10. **Métrica o forma de evaluación**  
   Propón al menos una forma de evaluar el sistema. Por ejemplo:
   - accuracy / F1
   - Recall@K
   - exact match
   - BLEU / ROUGE
   - evaluación cualitativa o análisis de error

#### Extensión sugerida
Entre **250 y 400 palabras**.

#### Formato de entrega
Entregar en un archivo Markdown o PDF con el nombre:

`ApellidoNombre-Actividad1-MCC225.md`

o

`ApellidoNombre-Actividad1-MCC225.pdf`

#### Plantilla de respuesta
```md
### Propuesta de problema multimodal

**Estudiante:**
**Título del problema:**

#### 1. Contexto

#### 2. Modalidades involucradas

#### 3. Entrada y salida esperada

#### 4. Tipo de tarea principal
(Clasificación / Retrieval/VQA / Generación / Mixta)

#### 5. Por qué es multimodal

#### 6. Posible fuente de datos

#### 7. Enfoque base o modelo tentativo

#### 8. Forma de evaluación
```

#### Recomendación

Elijan un problema **acotado, verificable y demostrable**. Es preferible una propuesta simple pero bien definida que una idea demasiado amplia y difícil de implementar.
