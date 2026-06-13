**Estudiante:**
**Título de la microtarea:**
Alineamiento imagen-texto mediante embeddings compartidos y similitud coseno usando OpenCLIP
#### 1. Problema elegido
Dada una imagen y un conjunto de descripciones textuales, identificar cuál descripción corresponde mejor a la imagen. De forma inversa, dada una consulta textual, recuperar la imagen más relevante. Este problema es conocido como recuperación imagen-texto y constituye una tarea fundamental en sistemas multimodales.
#### 2. Dataset o conjunto de ejemplo
conjunto de imágenes acompañadas de descripciones textuales (captions) de frames de ActivityNet

#### 3. Representación textual
Las descripciones fueron procesadas mediante el encoder de texto de OpenCLIP. Cada caption se transforma en un embedding denso de dimensión fija que captura información semántica del contenido textual.
#### 4. Representación visual
Las imágenes fueron procesadas mediante el encoder visual de OpenCLIP. Cada imagen se representa mediante un embedding de dimensión fija en el mismo espacio latente que los embeddings de texto.
#### 5. Espacio compartido o estrategia de comparación
OpenCLIP proyecta imágenes y textos en un espacio compartido de embeddings. La comparación entre ambas modalidades se realiza mediante similitud coseno.
#### 6. Métrica o criterio de evaluación
Recall@K (R@1, R@5 y R@10), que miden la frecuencia con que la respuesta correcta aparece entre los K primeros resultados recuperados.
#### 7. Resultados
El modelo logró asociar correctamente imágenes y descripciones en la mayoría de los ejemplos evaluados. Sin embargo se debe considerar que es una muestra pequeña de 33 videos.
#### 8. Limitaciones y análisis de error
Los principales errores aparecieron cuando distintas imágenes compartían elementos visuales similares o cuando las descripciones eran ambiguas y poco específicas.Un conjunto pequeño de 33 videos puede generar rankings menos robustos.
#### 9. Relación con la Actividad 1
Esta microtarea constituye la base conceptual de la Actividad 1. Mientras que aquí se estudia el alineamiento imagen-texto mediante embeddings compartidos y similitud coseno, en la Actividad 1 se extiende el mismo principio al caso video-texto utilizando modelos multimodales como OpenCLIP y X-CLIP para recuperación de eventos deportivos en ambas direcciones (texto→video y video→texto). El retrieval multimodal empleado en videos se fundamenta en los mismos conceptos de representación conjunta y comparación semántica aprendidos en esta actividad.

### Ejercicios de Repaso
* One-Hot representa cada palabra mediante un vector único, mientras que Bag of Words representa un documento mediante frecuencias de palabras.
* TF-IDF mejora Bag of Words asignando mayor importancia a términos informativos y menor peso a palabras muy frecuentes.
* Los n-gramas permiten conservar expresiones compuestas como "tarjeta roja" o "tiro libre" en eventos deportivos.
* Las subpalabras ayudan a representar términos raros o desconocidos dividiéndolos en fragmentos más pequeños.
* Los embeddings permiten capturar similitud semántica entre palabras, oraciones e incluso modalidades diferentes.
* OpenCLIP proyecta imágenes y texto a un espacio compartido de embeddings para facilitar el alineamiento multimodal.
* La similitud coseno permite medir la cercanía semántica entre representaciones visuales y textuales.
* El retrieval multimodal recupera las imágenes más relevantes para una consulta textual o viceversa.
* Estos conceptos sirven como base para tareas más complejas de recuperación video-texto y texto-video en eventos deportivos.
