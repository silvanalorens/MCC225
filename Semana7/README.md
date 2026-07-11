### **Atención, Transformers y entrada a modelos fundacionales multimodales**


Esta semana introduce los fundamentos de atención y Transformers como base para comprender modelos fundacionales modernos, incluyendo arquitecturas textuales y multimodales. 
El objetivo no es todavía realizar un tratamiento posgradual completo de los modelos visión-lenguaje, sino construir la ruta conceptual necesaria para estudiar posteriormente arquitecturas 
como CLIP, BLIP, BLIP-2, Flamingo, CoCa, LLaVA y modelos fundacionales multimodales recientes.

La semana está organizada de forma progresiva. Primero se revisan los mecanismos de atención desde una perspectiva didáctic, luego se estudia el bloque Transformer base, después se introducen variantes modernas de atención 
usadas en LLMs y finalmente se conecta el tema con modelos fundacionales y arquitecturas de comprensión/generación multimodal.

#### Prerrequisitos

Para aprovechar esta semana se recomienda manejar:

* álgebra lineal básica: vectores, matrices, producto punto y multiplicación matricial,
* Python básico,
* nociones iniciales de PyTorch,
* conceptos generales de redes neuronales,
* idea general de embeddings o representaciones vectoriales.

No se asume que el estudiante haya llevado previamente un curso completo de atención. Por eso se incluye una carpeta de repaso.

#### Ruta recomendada de estudio

##### 1. Repaso de atención clásica

Archivo:

```text
Repaso/Seq2seq_atencion_transformers.ipynb
```

Este cuaderno introduce los mecanismos clásicos de atención y construye el puente hacia self-attention. Se estudian conceptos como:

* atención en modelos Seq2Seq,
* atención global,
* atención local,
* atención jerárquica,
* consultas, claves y valores,
* self-attention,
* multi-head attention básica.

Este material es fundamental para entender los cuadernos posteriores. La idea central que debe quedar clara es que la atención permite que cada token construya una representación contextualizada usando información relevante de otros tokens.

##### 2. Transformer base

Archivo:

```text
Cuaderno11-MCC225.ipynb
```

Este cuaderno desarrolla la arquitectura Transformer como bloque fundamental de los modelos modernos. 

Temas principales:

* embeddings,
* codificación posicional,
* self-attention,
* multi-head attention,
* conexiones residuales,
* normalización,
* bloques encoder,
* bloques decoder,
* máscara causal,
* generación autoregresiva.

Este cuaderno es el eje técnico de la semana. Su objetivo es que el estudiante entienda cómo la atención se convierte en una arquitectura completa.

##### 3. Atención moderna en modelos actuales

Archivo:

```text
Repaso/Atencion_moderna_modelos.ipynb
```

Este cuaderno presenta variantes modernas usadas en LLMs y modelos de contexto largo.

Temas principales:

* Multi-Head Attention como punto de partida,
* KV cache,
* Grouped-Query Attention,
* Multi-Head Latent Attention,
* Sliding Window Attention,
* sparse attention,
* gated attention,
* QK-Norm,
* partial RoPE,
* hybrid attention.

Este material no reemplaza al cuaderno base de Transformers. Su función es mostrar cómo se modifica la atención para reducir memoria, mejorar inferencia y manejar contextos largos.

##### 4. Familias de modelos Transformer

Archivo:

```text
Cuaderno12-MCC225.ipynb
```

Este cuaderno debe usarse como puente hacia modelos fundacionales. Su función es comparar familias arquitectónicas:

* modelos encoder-only,
* modelos decoder-only,
* modelos encoder-decoder,
* modelos de comprensión,
* modelos generativos,
* modelos de resumen, traducción o generación condicionada.

En esta parte se puede ubicar conceptualmente a modelos como BERT, GPT y BART. Aquí es importante  entender que BERT representa la familia encoder-only, GPT la familia decoder-only 
y BART/T5 la familia encoder-decoder.

##### 5. Entrada a modelos multimodales

Archivo:

```text
Cuaderno13_MCC225.ipynb
```

Este cuaderno introduce el paso de Transformers textuales a modelos multimodales. Su objetivo es conectar atención, embeddings y modelos fundacionales con entradas de más de una modalidad.

Temas esperados:

* representación de imágenes como secuencias de patches,
* representación de texto como tokens,
* alineamiento imagen-texto,
* modelos de comprensión multimodal,
* modelos de generación multimodal,
* atención visual-semántica,
* recuperación imagen-texto,
* captioning,
* VQA,
* conexión conceptual con CLIP, BLIP y BLIP-2.

Este cuaderno funciona como una introducción. El análisis posgradual de papers y arquitecturas multimodales se realizará después.

#### Resultado esperado

Al terminar esta semana, el estudiante debería poder:

* explicar qué hacen `Q`, `K` y `V`,
* interpretar una matriz de atención,
* distinguir self-attention de cross-attention,
* explicar por qué se usa multi-head attention,
* describir el bloque Transformer,
* diferenciar encoder-only, decoder-only y encoder-decoder,
* reconocer por qué los LLMs modernos modifican la atención,
* identificar la función de GQA, MLA, sliding window attention y sparse attention,
* explicar de forma introductoria cómo se conectan texto e imagen en modelos multimodales,
* ubicar modelos como BERT, GPT, BART, CLIP, BLIP y BLIP-2 dentro de una taxonomía general.

##### Nota pedagógica

Esta semana no pretende agotar el estudio de modelos fundacionales multimodales. Su función es construir la base necesaria para que, en semanas posteriores, los estudiantes puedan leer papers y analizar arquitecturas multimodales a nivel de posgrado con mayor rigor.
