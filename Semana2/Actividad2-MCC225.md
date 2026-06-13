## Actividad 2-MCC225

### Línea base reproducible de alineamiento visual-semántico temprano

#### Objetivo

Implementar y explicar una **línea base reproducible** de alineamiento visual-semántico temprano a partir del cuaderno principal de la clase 2 y los cuadernos de repaso de la semana 2. 
La actividad busca que cada estudiante comprenda, con evidencia en código, cómo se construyen representaciones de texto e imagen, cómo se comparan en un espacio común y cómo se evalúa un sistema simple de recuperación o emparejamiento imagen-texto.

#### Instrucciones

Cada estudiante debe entregar **1 notebook original o adaptado** en el que implemente una línea base pequeña pero funcional de alineamiento visual-semántico. 
La actividad debe apoyarse en:

- `Cuaderno2-MCC225.ipynb` como cuaderno principal de clase.
- Los cuadernos de repaso de `Semana2/Cuadernos_de_repaso` como material de nivelación y soporte.

La entrega debe responder, como mínimo, a los siguientes componentes:

1. **Título de la actividad**  
   Escribe un título breve y claro para tu notebook.

2. **Problema o microtarea elegida**  
   Define una tarea acotada relacionada con alineamiento imagen-texto. Puede ser, por ejemplo:
   - emparejamiento imagen-texto,
   - recuperación simple texto->imagen o imagen->texto,
   - comparación de representaciones visuales y textuales,
   - análisis de similitud semántica multimodal.

3. **Dataset o conjunto de ejemplo**  
   Usa un conjunto pequeño y reproducible. Puede ser:
   - un dataset sintético construido por ti,
   - un subconjunto pequeño de ejemplos curados,
   - datos incluidos en librerías estándar,
   - imágenes simples con descripciones o etiquetas textuales.

   No se requiere un dataset grande. Se prioriza claridad conceptual y reproducibilidad.

4. **Representación textual**  
   Implementa al menos una representación textual y explíquela brevemente. Por ejemplo:
   - one-hot,
   - Bag of Words,
   - TF-IDF,
   - embedding promedio,
   - representación distribuida simple.

   Debes justificar por qué esa representación es razonable para la tarea elegida.

5. **Representación visual**  
   Implementa al menos una representación visual y explíquela brevemente. Por ejemplo:
   - histograma tipo BoVW simplificado,
   - descriptores locales o globales,
   - features extraídas con una CNN preentrenada,
   - representación regional simplificada,
   - vectores visuales construidos sobre imágenes pequeñas o sintéticas.

6. **Espacio compartido o mecanismo de comparación**  
   Debes mostrar explícitamente cómo texto e imagen se vuelven comparables. Esto puede hacerse, por ejemplo, mediante:
   - proyecciones lineales,
   - concatenación seguida de una transformación,
   - similitud coseno directa si ambas modalidades ya están vectorizadas de forma compatible,
   - una capa lineal aprendible para una o ambas modalidades.

7. **Similitud y criterio de entrenamiento o comparación**  
   Debes incluir uno de estos niveles:
   - **mínimo requerido:** matriz de similitud y análisis sin entrenamiento fuerte;
   - **recomendado:** una pérdida de margen (`margin ranking loss`) con pares positivos y negativos;
   - **opcional avanzado:** una pérdida contrastiva tipo InfoNCE o in-batch contrastive loss.

8. **Evaluación mínima**  
   Reporta al menos una forma simple de evaluación. Por ejemplo:
   - top-1 o top-k retrieval,
   - Recall@K,
   - ranking correcto de pares,
   - visualización de matriz de similitud,
   - análisis cualitativo de ejemplos correctos e incorrectos.

9. **Análisis de resultados y limitaciones**  
   Incluye una sección breve donde expliques:
   - qué funcionó,
   - qué limitaciones tiene tu línea base,
   - qué diferencia habría con modelos posteriores como CLIP u otros métodos contrastivos modernos.

10. **Relación con la Actividad 1**  
   Cierra con un párrafo explicando si esta línea base podría servir como antecedente técnico para el problema multimodal que propusiste en la Actividad 1.

#### Requisitos mínimos del notebook

El notebook debe contener, como mínimo, estas secciones:

1. Introducción del problema.  
2. Descripción del dataset o ejemplos.  
3. Representación textual.  
4. Representación visual.  
5. Comparación o alineamiento en espacio compartido.  
6. Evaluación básica.  
7. Análisis de errores o limitaciones.  
8. Conclusión.

#### Requisitos de código

- El notebook debe ejecutarse de principio a fin sin depender de rutas locales privadas.
- Debe fijar semillas cuando corresponda.
- Debe incluir comentarios suficientes para entender cada bloque.
- Debe generar al menos una salida interpretable: tabla, matriz, gráfico o ranking.
- Debe indicar claramente qué partes son obligatorias y cuáles son exploratorias.

#### Extensión sugerida

- **Notebook:** entre 1 y 3 secciones de código principal bien comentadas por bloque conceptual.
- **Explicación escrita dentro del notebook:** equivalente aproximado a **500-900 palabras** distribuidas en celdas Markdown.

#### Formato de entrega

Entregar en un archivo Jupyter Notebook con el nombre:

`ApellidoNombre-Actividad2-MCC225.ipynb`

Opcionalmente, puede acompañarse de una versión exportada en PDF:

`ApellidoNombre-Actividad2-MCC225.pdf`

#### Plantilla de respuesta

```markdown
### Actividad 2-MCC225
#### Línea base reproducible de alineamiento visual-semántico temprano

**Estudiante:**
**Título de la microtarea:**

#### 1. Problema elegido

#### 2. Dataset o conjunto de ejemplo

#### 3. Representación textual

#### 4. Representación visual

#### 5. Espacio compartido o estrategia de comparación

#### 6. Métrica o criterio de evaluación

#### 7. Resultados

#### 8. Limitaciones y análisis de error

#### 9. Relación con la Actividad 1
```

#### Recomendación

Elige una línea base **simple, verificable y bien explicada**. En esta etapa vale más una implementación pequeña pero conceptualmente correcta que una solución ambiciosa y poco reproducible. 
La meta de la actividad es consolidar la intuición sobre **representación**, **similitud**, **alineamiento temprano** y **evaluación básica** antes de pasar a modelos contrastivos más potentes.

#### Sugerencia de apoyo

Puedes reutilizar, adaptar o combinar ideas de:

- `Representaciones_de_texto.ipynb`
- `Semantica_vectorial_embeddings.ipynb`
- `Integrando_word2vec.ipynb`
- `Representacion_visual_multimodal.ipynb`
- `Cuaderno2-MCC225.ipynb`

pero la entrega final debe estar integrada como un **único notebook coherente**.
