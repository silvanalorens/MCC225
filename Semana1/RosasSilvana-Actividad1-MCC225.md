### Propuesta de problema multimodal

**Estudiante:**
Silvana Lorens Rosas Oquendo
**Título del problema:**
"Sistema multimodal para recuperación video-texto y texto-video de eventos deportivos mediante OpenCLIP y X-CLIP": Se cambia por obtener dataset público en hugging face ActivityNet, y por realizarse prueba de concepto con 33 videos extraidos del dataset. Antes(“Sistema multimodal para detección de comportamiento atipico usando video y sensores de temperatura”).
#### 1. Contexto
Actualmente existen grandes cantidades de contenido deportivo publicado en plataformas web, redes sociales y repositorios multimedia. Sin embargo, encontrar rápidamente videos específicos a partir de una descripción textual, o localizar descripciones relevantes a partir de un video, sigue siendo una tarea compleja. Este problema aparece en buscadores multimedia, sistemas de recomendación y plataformas de análisis deportivo. En este proyecto se estudia la recuperación video-texto y texto-video utilizando modelos multimodales como OpenCLIP y X-CLIP sobre un conjunto de videos deportivos con sus respectivas descripciones.

#### 2. Modalidades involucradas
Video (imagen en secuencia)
texto

#### 3. Entrada y salida esperada
Entrada:

Secuencia de video de youtube de dataset ActivityNet


Salida:

Etiqueta de evento: "swimming", "dancing"
Segmentos de video donde ocurre el evento


#### 4. Tipo de tarea principal

Retrieval
El sistema recupera videos con los eventos solicitados por texto.

#### 5. Por qué es multimodal
Se tiene informacion visual (movimiento, presencia de personas) con datos físicos 
#### 6. Posible fuente de datos
Datasets públicos de vigilancia

#### 7. Enfoque base o modelo tentativo
Modelo de detección de objetos (YOLO o similar)
Extracción de características de movimiento
Fusión con datos de sensores mediante reglas CLIP o VideoClip para representación conjunta

#### 8. Forma de evaluación
Recall para eventos
Matriz de similaridad