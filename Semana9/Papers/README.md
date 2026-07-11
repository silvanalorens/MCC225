### Bibliografía de Semana9

#### Criterio

Esta carpeta reúne las fuentes base para la Semana 9 de MCC225, centrada en confiabilidad, sesgo, explicabilidad, fairness, gobernanza y uso responsable de modelos fundacionales y sistemas multimodales.

A diferencia de la Semana 8, donde el foco principal estaba en evaluación, métricas, reproducibilidad y análisis de error, esta semana desplaza la discusión hacia la gestión de riesgos, la transparencia, la equidad, la responsabilidad académica y la documentación necesaria para sostener afirmaciones responsables sobre un sistema multimodal.

Las fuentes fueron seleccionadas porque permiten estudiar la confiabilidad desde varias perspectivas complementarias:

- responsabilidad en modelos fundacionales
- explicabilidad e interpretabilidad en MLLMs
- fairness en tareas multimodales de alto impacto
- confianza multimodal: veracidad, robustez, seguridad, fairness y privacidad
- gestión de riesgos para IA generativa
- principios internacionales de IA confiable
- sistemas de gestión de IA
- regulación basada en riesgo.

#### Papers y fuentes de referencia

| Referencia base | Título completo | Autores o institución | Año | Tipo | Fuente oficial | Uso en el curso | Estado |
|---|---|---:|---:|---|---|---|---|
| Reliable and Responsible Foundation Models | Reliable and Responsible Foundation Models: A Comprehensive Survey | Yang et al. | 2026 | Survey | https://arxiv.org/abs/2602.08145 | Marco amplio para conectar sesgo, seguridad, privacidad, incertidumbre, explicabilidad, alucinaciones, alineamiento y limitaciones de uso. | Verificado |
| Explainable and Interpretable MLLMs | Explainable and Interpretable Multimodal Large Language Models: A Comprehensive Survey | Dang et al. | 2024 | Survey | https://arxiv.org/abs/2412.02104 | Base técnica para distinguir explicabilidad e interpretabilidad en modelos multimodales grandes. | Verificado |
| FMBench | FMBench: Benchmarking Fairness in Multimodal Large Language Models on Medical Tasks | Wu et al. | 2024 | Benchmark | https://arxiv.org/abs/2410.01089 | Caso de estudio para evaluar fairness en tareas médicas multimodales mediante atributos demográficos y métricas de equidad. | Verificado |
| Unveiling Trust in MLLMs | Unveiling Trust in Multimodal Large Language Models: Evaluation, Analysis, and Mitigation | Zhang et al. | 2025 | Evaluación y mitigación | https://arxiv.org/abs/2508.15370 | Taxonomía de confianza multimodal: veracidad, robustez, seguridad, fairness, privacidad y riesgos cross-modal. | Verificado |
| NIST AI RMF Generative AI Profile | Artificial Intelligence Risk Management Framework: Generative Artificial Intelligence Profile | NIST | 2024 | Marco de gestión de riesgos | https://doi.org/10.6028/NIST.AI.600-1 | Guía operativa para gobernar, mapear, medir y gestionar riesgos de IA generativa durante el ciclo de vida. | Verificado |
| OECD AI Principles | OECD AI Principles | OECD | Vigente | Principios internacionales | https://www.oecd.org/en/topics/sub-issues/ai-principles.html | Principios para IA confiable centrada en derechos humanos, transparencia, robustez, responsabilidad e innovación inclusiva. | Verificado |
| ISO/IEC 42001:2023 | Information technology - Artificial intelligence - Management system | ISO | 2023 | Estándar | https://www.iso.org/standard/42001 | Estándar de sistema de gestión de IA para organizar políticas, roles, documentación, monitoreo y mejora continua. | Verificado |
| EU AI Act 2024/1689 | Regulation (EU) 2024/1689 | European Parliament and Council of the European Union | 2024 | Regulación | https://eur-lex.europa.eu/eli/reg/2024/1689/oj/eng | Marco regulatorio basado en riesgo, útil para discutir documentación técnica, transparencia, supervisión humana y obligaciones diferenciadas. | Verificado |

#### Nota para estudiantes

Estas fuentes no deben leerse como una lista aislada de regulaciones o surveys. Deben leerse como una metodología para pasar de una evaluación técnica básica a una evaluación responsable de sistemas multimodales.

#### Ruta sugerida de lectura

1. Leer Reliable and Responsible Foundation Models para obtener una visión amplia de riesgos en modelos fundacionales.
2. Leer Explainable and Interpretable MLLMs para diferenciar explicación, interpretabilidad, evidencia y mecanismos internos.
3. Leer FMBench para estudiar fairness en un dominio multimodal de alto impacto.
4. Leer Unveiling Trust in MLLMs para organizar la confianza multimodal en dimensiones técnicas.
5. Leer NIST AI RMF Generative AI Profile para traducir riesgos en acciones documentables.
6. Leer OECD AI Principles para conectar el proyecto con principios internacionales de IA confiable.
7. Leer ISO/IEC 42001:2023 para entender la lógica de gestión, roles, documentación y mejora continua.
8. Leer EU AI Act 2024/1689 para comprender el enfoque basado en riesgo y su traducción pedagógica.

#### Uso esperado en MCC225

Al terminar la lectura, el estudiante debe poder construir una ficha de confiabilidad responsable para un sistema multimodal que incluya:

- propósito del sistema
- alcance y usos no permitidos
- fuentes de datos
- métricas de desempeño
- análisis de errores por categoría
- revisión de alucinaciones o confabulaciones
- evaluación de robustez
- discusión de sesgo o cobertura de subgrupos
- evidencia de explicabilidad o trazabilidad
- revisión de privacidad y datos sensibles
- limitaciones reales
- conclusión proporcional a la evidencia experimental

#### Relación con el trabajo integrador

En el informe final de MCC225, estas fuentes deben aparecer como base para una sección explícita de confiabilidad y uso responsable. Una estructura mínima puede ser:

1. descripción del modelo o sistema
2. evaluación cuantitativa
3. análisis cualitativo de errores
4. confiabilidad y robustez
5. sesgo y cobertura de datos
6. explicabilidad y trazabilidad
7. privacidad y uso responsable
8. limitaciones y trabajo futuro.

#### Advertencia metodológica

Una métrica alta no demuestra por sí sola que un sistema sea confiable. La confiabilidad exige analizar fallas, severidad, contexto, sesgo, robustez, supervisión humana, trazabilidad y límites de uso.

Tampoco debe afirmarse que un sistema no tiene sesgo si no se midió. En proyectos pequeños, puede realizarse una exploración cualitativa honesta, pero debe declararse explícitamente que no reemplaza una evaluación estadística completa de fairness.
