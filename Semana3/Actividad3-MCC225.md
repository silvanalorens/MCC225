### Actividad 3-MCC225

#### Síntesis comparativa y ruta de diseño multimodal

Esta actividad continúa directamente la secuencia de las dos anteriores:

- **Actividad 1:** definir un problema multimodal acotado, con modalidades, tarea, datos y métrica.
- **Actividad 2:** construir una línea base reproducible de alineamiento visual-semántico temprano.
- **Actividad 3 (esta entrega):** revisar comparativamente las familias de modelos estudiadas en los **Cuadernos 3 al 8** y proponer una **ruta de diseño razonada** para el problema planteado en la Actividad 1.

La meta ya no es solo implementar una línea base, sino **aprender a decidir** qué familia de arquitectura tiene más sentido según el tipo de problema, el nivel de interacción entre modalidades, la temporalidad, la alineación o desalineación entre señales y el costo computacional esperable.

#### Objetivos de aprendizaje
Al finalizar esta actividad, cada estudiante debería poder:

1. Explicar la progresión conceptual del bloque:
   **fusión -> fusión con transformers -> deep fusion -> alineamiento contrastivo -> video-texto temporal -> atención crossmodal no alineada**.
2. Comparar arquitecturas multimodales según:
   - punto de interacción,
   - tipo de tarea dominante,
   - ventajas,
   - limitaciones,
   - costo relativo,
   - casos de uso.
3. Interactuar de forma guiada con los cuadernos del bloque y registrar observaciones propias.
4. Justificar cuál sería la **siguiente ruta experimental** para su problema de la Actividad 1, usando como antecedente la línea base de la Actividad 2.


#### Material obligatorio de referencia

La actividad debe apoyarse en estos materiales del curso:

- `Semana3/Cuadernos/Cuaderno3-MCC225.ipynb`
- `Semana3/Cuadernos/Cuaderno4-MCC225.ipynb`
- `Semana3/Cuadernos/Cuaderno5-MCC225.ipynb`
- `Semana3/Cuadernos/Cuaderno6-MCC225.ipynb`
- `Semana3/Cuadernos/Cuaderno7-MCC225.ipynb`
- `Semana3/Cuadernos/Cuaderno8-MCC225.ipynb`
- `Plantilla-Actividad3-MCC225.ipynb` como base obligatoria de trabajo.

#### Instrucciones generales

Cada estudiante debe entregar **un notebook integrado y comentado**, construido a partir de la **plantilla entregada junto con esta actividad**, en el que desarrolle una **síntesis comparativa** del bloque y la conecte con su propio problema multimodal.

La entrega no requiere reproducir por completo todos los experimentos de los cuadernos 3 al 8.  
Lo que sí exige es demostrar, con evidencia conceptual y al menos algunas interacciones en código, que el estudiante entiende:

- qué problema aborda cada familia de modelos,
- qué cambia cuando la interacción multimodal ocurre antes, durante o después del procesamiento,
- por qué el alineamiento contrastivo no es lo mismo que la fusión para clasificación,
- qué dificultades nuevas aparecen cuando entra la temporalidad,
- y por qué la no alineación entre modalidades exige mecanismos más expresivos como atención crossmodal.


#### Producto a entregar

Entregar **1 notebook Jupyter** con el nombre:

`ApellidoNombre-Actividad3-MCC225.ipynb`


**La plantilla entregada debe usarse como base de la entrega.** Puede ampliarse, reorganizarse o enriquecerse, pero no reemplazarse por un notebook vacío.

#### Estructura mínima obligatoria del notebook

##### 1. Título y contexto
Incluye:

- nombre de la actividad,
- nombre del estudiante,
- título breve de su problema multimodal,
- referencia explícita a la Actividad 1.

En esta sección debes recuperar en **3 a 5 líneas** el problema que propusiste en la Actividad 1.


##### 2. Conexión con la Actividad 2
Resume en un párrafo breve:

- qué línea base implementaste en la Actividad 2,
- qué aprendiste de ella,
- qué limitaciones detectaste,
- y por qué ya no basta esa solución para avanzar.

Aquí no se pide repetir el notebook anterior, sino usarlo como **punto de partida técnico**.

##### 3. Línea de tiempo conceptual del bloque
Construye una síntesis breve de la progresión entre los cuadernos 3 al 8.

Como mínimo, debes incluir una tabla o esquema que responda para cada etapa:

- **cuaderno**,
- **familia de modelo**,
- **pregunta central**,
- **tipo de tarea dominante**,
- **qué aporta frente a la etapa anterior**.

Se espera una lectura del bloque más cercana a esta lógica:

- **Cuadernos 3, 4 y 5:** cómo fusionar modalidades cada vez con mayor capacidad de interacción.
- **Cuaderno 6:** cómo alinear modalidades en un espacio común para retrieval y matching.
- **Cuaderno 7:** cómo extender el problema a video-texto con temporalidad.
- **Cuaderno 8:** cómo modelar secuencias multimodales no alineadas mediante atención crossmodal.

#### 4. Tabla comparativa obligatoria
Debes construir una tabla comparativa con al menos estas familias:

- Late Fusion
- MMBT-Lite
- Deep Fusion Transformer
- Bi-encoder contrastivo
- VideoCLIP-lite o ALPRO-lite temporal
- MulT-lite o SPT-lite

La tabla debe incluir como mínimo estas columnas:

1. Familia / modelo
2. Cuaderno de referencia
3. Tarea dominante
4. Punto de interacción entre modalidades
5. Fortaleza principal
6. Limitación principal
7. Costo relativo estimado
8. ¿En qué tipo de proyecto lo usaría?

No se busca exactitud de benchmark, sino **lectura metodológica argumentada**.

#### 5. Interacción guiada con los cuadernos
Esta es la parte central de la actividad.

Debes interactuar con **al menos tres cuadernos** del bloque y documentar qué hiciste y qué observaste.  
No basta con decir "lo revisé",  debes registrar una interacción concreta.

##### Interacción A: familia de fusión
Elige **uno** entre los cuadernos 3, 4 o 5 y realiza una intervención pequeña, por ejemplo:

- comparar dos variantes de fusión,
- cambiar una configuración simple,
- analizar una tabla o salida del cuaderno,
- registrar cuándo una modalidad parece dominar a la otra.

##### Interacción B: familia de alineamiento o temporalidad
Elige **uno** entre los cuadernos 6 o 7 y realiza una intervención pequeña, por ejemplo:

- comparar negativos aleatorios vs. semi-duros,
- revisar un ranking o métrica de retrieval,
- analizar un caso donde el problema temporal cambia la interpretación del positivo.

##### Interacción C: no alineación y decisión razonada
Debes usar el **Cuaderno 8** para responder:

- ¿por qué Late Fusion deja de ser suficiente en secuencias no alineadas?
- ¿qué ventaja conceptual trae la atención crossmodal?
- ¿qué familia parece más razonable para tu problema y por qué?

Para cada interacción documenta:

- cuaderno usado,
- bloque o sección revisada,
- cambio, prueba o lectura realizada,
- evidencia observada,
- interpretación en 4 a 8 líneas.


#### 6. Mini simulador o regla de decisión
A partir de la síntesis de los **Cuadernos 3 al 8**, debes implementar una pequeña pieza de código que ayude a responder:

> "Según las características del problema, ¿qué familia de arquitectura parece más adecuada?"

Puede ser cualquiera de estas opciones:

- una función `recommend_architecture(...)`,
- un sistema simple de puntajes,
- una tabla de decisión,
- un flujo lógico programado,
- una visualización comparativa.

La entrada debe considerar al menos **cuatro** criterios, por ejemplo:

- tipo de tarea,
- necesidad de interacción fina,
- presencia de temporalidad,
- presencia de no alineación,
- restricción computacional,
- necesidad de retrieval a gran escala.

La salida debe devolver una recomendación razonada de **1 o 2 familias**.

#### 7. Ruta propuesta para tu proyecto

Vuelve al problema de la Actividad 1 y redacta una propuesta de continuación que incluya:

1. **Familia de arquitectura elegida**
2. **Por qué esa familia tiene sentido**
3. **Qué conservarías de la línea base de la Actividad 2**
4. **Qué cambiarías**
5. **Qué métrica usarías**
6. **Cuál sería el siguiente experimento pequeño y reproducible**

Esta sección funciona como un **puente entre revisión conceptual y diseño experimental**.


#### 8. Limitaciones, dudas y preguntas abiertas
Cierra con una sección breve donde respondas:

- ¿qué parte del bloque te resultó más clara?
- ¿qué parte todavía te genera dudas?
- ¿qué familia de modelo te gustaría estudiar más a fondo?
- ¿qué riesgo metodológico ves en tu propia propuesta?


##### Requisitos mínimos de código

El notebook debe:

- ejecutarse de principio a fin sin depender de rutas locales privadas,
- incluir comentarios suficientes para entender cada bloque,
- contener al menos **una tabla** y **una figura o visualización**,
- incluir al menos **una función implementada por el estudiante**,
- mostrar al menos **dos intervenciones o variaciones** sobre materiales de los cuadernos,
- separar claramente lo obligatorio de lo exploratorio.


#### Plantilla breve sugerida

```markdown
## Actividad 3-MCC225
### Síntesis comparativa y ruta de diseño multimodal

**Estudiante:**  
**Título del problema:**  

#### 1. Recuperación del problema de la Actividad 1

#### 2. Qué aprendí de la Actividad 2

#### 3. Línea de tiempo conceptual del bloque

#### 4. Tabla comparativa de familias

#### 5. Interacción guiada con cuadernos
##### 5.1 Interacción A
##### 5.2 Interacción B
##### 5.3 Interacción C

#### 6. Simulador o regla de decisión

#### 7. Ruta propuesta para mi proyecto

#### 8. Limitaciones y preguntas abiertas
```

#### Recomendación final

La meta de esta actividad no es "cubrir más modelos" por acumulación, sino aprender a responder una pregunta clave:

> **¿Qué familia de modelo conviene estudiar o implementar para un problema multimodal específico, y por qué?**

Es preferible una síntesis pequeña pero rigurosa, con decisiones bien justificadas, que una revisión amplia pero superficial.
