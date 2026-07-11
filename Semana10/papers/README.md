### Bibliografía de Semana10

#### Criterio

Esta carpeta reemplaza los PDFs externos por referencias bibliográficas verificables.

Los PDFs de papers no se versionan directamente en Git. Cada trabajo debe consultarse desde fuentes oficiales como arXiv, DOI, página del congreso, revista, editorial o sitio institucional de los autores.

La Semana 10 se centra en razonamiento multimodal, grounding, análisis de errores, alucinación, consistencia y verificación de evidencias. Por ello, los trabajos seleccionados cubren razonamiento con imagen y texto, preguntas científicas multimodales, grounding visual, grounding denso, evaluación de alucinaciones, consistencia lógica, modelos visión-lenguaje recientes y líneas futuras hacia modelos visión-lenguaje-acción.

#### Papers de referencia

| Referencia base | Título completo | Autores | Año | Fuente oficial | Uso en el curso | Estado |
|---|---|---|---:|---|---|---|
| Multimodal_CoT | Multimodal Chain-of-Thought Reasoning in Language Models | Zhuosheng Zhang, Aston Zhang, Mu Li, Hai Zhao, George Karypis, Alex Smola | 2023 | [arXiv](https://arxiv.org/abs/2302.00923), [GitHub](https://github.com/amazon-science/mm-cot) | Razonamiento multimodal con racionales y respuesta final separada | Verificado |
| ScienceQA | Learn to Explain: Multimodal Reasoning via Thought Chains for Science Question Answering | Pan Lu, Swaroop Mishra, Tony Xia, Liang Qiu, Kai-Wei Chang, Song-Chun Zhu, Oyvind Tafjord, Peter Clark, Ashwin Kalyan | 2022 | [arXiv](https://arxiv.org/abs/2209.09513), [Sitio oficial](https://scienceqa.github.io/) | Preguntas científicas multimodales con explicaciones, razonamiento y evidencia | Verificado |
| MMMU | MMMU: A Massive Multi-discipline Multimodal Understanding and Reasoning Benchmark for Expert AGI | Xiang Yue et al. | 2023 | [arXiv](https://arxiv.org/abs/2311.16502), [Sitio oficial](https://mmmu-benchmark.github.io/) | Benchmark avanzado para razonamiento multimodal con conocimiento experto y múltiples disciplinas | Verificado |
| KOSMOS2 | Kosmos-2: Grounding Multimodal Large Language Models to the World | Zhiliang Peng, Wenhui Wang, Li Dong, Yaru Hao, Shaohan Huang, Shuming Ma, Furu Wei | 2023 | [arXiv](https://arxiv.org/abs/2306.14824), [Proyecto](https://aka.ms/kosmos-2) | Grounding de lenguaje a regiones visuales mediante referencias y cajas delimitadoras | Verificado |
| Grounding_DINO | Grounding DINO: Marrying DINO with Grounded Pre-Training for Open-Set Object Detection | Shilong Liu et al. | 2023 | [arXiv](https://arxiv.org/abs/2303.05499), [GitHub](https://github.com/IDEA-Research/GroundingDINO) | Detección abierta guiada por texto, grounding de expresiones y evidencia visual localizable | Verificado |
| GLaMM | GLaMM: Pixel Grounding Large Multimodal Model | Hanoona Rasheed et al. | 2023 | [arXiv](https://arxiv.org/abs/2311.03356) | Grounding denso a nivel de píxel para conversaciones multimodales y segmentación asociada a texto | Verificado |
| POPE | Evaluating Object Hallucination in Large Vision-Language Models | Yifan Li, Yifan Du, Kun Zhou, Jinpeng Wang, Wayne Xin Zhao, Ji-Rong Wen | 2023 | [arXiv](https://arxiv.org/abs/2305.10355), [GitHub](https://github.com/RUCAIBox/POPE) | Evaluación de alucinación de objetos, falsos positivos visuales y grounding de respuestas | Verificado |
| HallusionBench | HallusionBench: An Advanced Diagnostic Suite for Entangled Language Hallucination and Visual Illusion in Large Vision-Language Models | Tianrui Guan et al. | 2023 | [arXiv](https://arxiv.org/abs/2310.14566), [GitHub](https://github.com/tianyi-lab/HallusionBench) | Diagnóstico de alucinación, ilusión visual, consistencia lógica y fallas de interpretación visual | Verificado |

#### Papers complementarios orientados al futuro

| Referencia base | Título completo | Autores | Año | Fuente oficial | Uso en el curso | Estado |
|---|---|---|---:|---|---|---|
| LLaVA_CoT | LLaVA-CoT: Let Vision Language Models Reason Step-by-Step | Guowei Xu, Peng Jin, Hao Li, Yibing Song, Lichao Sun, Li Yuan | 2024 | [arXiv](https://arxiv.org/abs/2411.10440) | Razonamiento multimodal estructurado por etapas: resumen, interpretación visual, razonamiento lógico y conclusión | Complementario |
| Visual_Sketchpad | Visual Sketchpad: Sketching as a Visual Chain of Thought for Multimodal Language Models | Yushi Hu, Weijia Shi, Xingyu Fu, Dan Roth, Mari Ostendorf, Luke Zettlemoyer, Noah A. Smith, Ranjay Krishna | 2024 | [arXiv](https://arxiv.org/abs/2406.09403), [Proyecto](https://visualsketchpad.github.io/) | Uso de bocetos, marcas, cajas y herramientas visuales como pasos intermedios de razonamiento | Complementario |
| MMMU_Pro | MMMU-Pro: A More Robust Multi-discipline Multimodal Understanding Benchmark | Xiang Yue et al. | 2024 | [arXiv](https://arxiv.org/abs/2409.02813) | Evaluación más robusta de razonamiento multimodal experto, reduciendo preguntas resolubles solo con texto | Complementario |
| MEGA_Bench | MEGA-Bench: Scaling Multimodal Evaluation to over 500 Real-World Tasks | Jiacheng Chen et al. | 2024 | [arXiv](https://arxiv.org/abs/2410.10563) | Evaluación de tareas multimodales reales con múltiples formatos de salida y métricas heterogéneas | Complementario |
| MME_RealWorld | MME-RealWorld: Could Your Multimodal LLM Challenge High-Resolution Real-World Scenarios that are Difficult for Humans? | Yi-Fan Zhang et al. | 2024 | [arXiv](https://arxiv.org/abs/2408.13257), [Proyecto](https://mme-realworld.github.io/) | Evaluación de modelos multimodales en imágenes de alta resolución y escenarios reales complejos | Complementario |
| Qwen2_5_VL | Qwen2.5-VL Technical Report | Shuai Bai et al. | 2025 | [arXiv](https://arxiv.org/abs/2502.13923) | Modelo visión-lenguaje moderno con localización, análisis documental, comprensión de video largo y capacidades de agente visual | Complementario |
| InternVL_2_5 | Expanding Performance Boundaries of Open-Source Multimodal Models with Model, Data, and Test-Time Scaling | Zhe Chen et al. | 2024 | [arXiv](https://arxiv.org/abs/2412.05271), [Demo](https://huggingface.co/spaces/OpenGVLab/InternVL) | Escalamiento de modelos multimodales abiertos mediante datos, tamaño de modelo y test-time scaling | Complementario |
| PaliGemma_2 | PaliGemma 2: A Family of Versatile VLMs for Transfer | Andreas Steiner et al. | 2024 | [arXiv](https://arxiv.org/abs/2412.03555) | Familia abierta de VLMs para transferencia, OCR, documentos, captioning fino y tareas visuales especializadas | Complementario |
| OpenVLA | OpenVLA: An Open-Source Vision-Language-Action Model | Moo Jin Kim et al. | 2024 | [arXiv](https://arxiv.org/abs/2406.09246) | Línea futura hacia modelos visión-lenguaje-acción, adaptación eficiente y control visomotor | Exploratorio |

#### Nota para estudiantes

Antes de citar un trabajo, se debe verificar la referencia completa en la fuente oficial. Esta lista sirve como guía de lectura del curso y no reemplaza una ficha bibliográfica formal.

La Semana 10 no debe leerse como una colección de benchmarks aislados. El objetivo es entender cómo un modelo multimodal razona, cómo conecta su respuesta con evidencia visual, cuándo inventa evidencia y cómo se pueden clasificar sus errores.

#### Ruta sugerida de lectura

1. Leer Multimodal Chain-of-Thought para introducir razonamiento multimodal con racionales.
2. Leer ScienceQA para conectar preguntas multimodales, explicaciones y razonamiento científico.
3. Leer MMMU y MMMU-Pro para analizar razonamiento multimodal experto.
4. Leer KOSMOS-2 para introducir grounding de lenguaje a regiones visuales.
5. Leer Grounding DINO para estudiar detección abierta guiada por texto.
6. Leer GLaMM para estudiar grounding denso y respuestas asociadas a máscaras de segmentación.
7. Leer POPE y HallusionBench para evaluar alucinación, consistencia e ilusión visual.
8. Leer LLaVA-CoT, Visual Sketchpad y MEGA-Bench como líneas actuales de razonamiento y evaluación multimodal.
9. Leer Qwen2.5-VL, InternVL 2.5, PaliGemma 2 y OpenVLA como puente hacia modelos recientes y sistemas orientados a acción.

