### Bibliografía de Semana11

#### Criterio

Esta carpeta reemplaza los PDFs externos por referencias bibliográficas verificables.

Los PDFs de papers no se versionan directamente en Git. Cada trabajo debe consultarse desde fuentes oficiales como arXiv, DOI, página del congreso, revista, editorial o sitio institucional de los autores.

La Semana 11 se centra en adaptación eficiente de modelos. El foco está en prompting estructurado, ajuste ligero, PEFT, cuantización y reducción de costo computacional. Por ello, los trabajos seleccionados cubren adapters, prompt tuning, prefix tuning, LoRA, QLoRA, visual instruction tuning, adaptación multimodal eficiente, cuantización de modelos grandes y líneas recientes de reducción de memoria.

#### Papers de referencia

| Referencia base | Título completo | Autores | Año | Fuente oficial | Uso en el curso | Estado |
|---|---|---|---:|---|---|---|
| Adapters | Parameter-Efficient Transfer Learning for NLP | Neil Houlsby, Andrei Giurgiu, Stanislaw Jastrzebski, Bruna Morrone, Quentin de Laroussilhe, Andrea Gesmundo, Mona Attariyan, Sylvain Gelly | 2019 | [arXiv](https://arxiv.org/abs/1902.00751) | Fundamento de módulos adaptadores con modelo base congelado y pocos parámetros por tarea | Verificado |
| Prefix_Tuning | Prefix-Tuning: Optimizing Continuous Prompts for Generation | Xiang Lisa Li, Percy Liang | 2021 | [arXiv](https://arxiv.org/abs/2101.00190) | Prompting continuo para generación con parámetros congelados y prefijos entrenables | Verificado |
| Prompt_Tuning | The Power of Scale for Parameter-Efficient Prompt Tuning | Brian Lester, Rami Al-Rfou, Noah Constant | 2021 | [arXiv](https://arxiv.org/abs/2104.08691) | Soft prompts entrenables como alternativa ligera al ajuste completo del modelo | Verificado |
| LoRA | LoRA: Low-Rank Adaptation of Large Language Models | Edward J. Hu, Yelong Shen, Phillip Wallis, Zeyuan Allen-Zhu, Yuanzhi Li, Shean Wang, Lu Wang, Weizhu Chen | 2021 | [arXiv](https://arxiv.org/abs/2106.09685), [GitHub](https://github.com/microsoft/LoRA) | Adaptación de bajo rango con pesos base congelados y matrices entrenables pequeñas | Verificado |
| QLoRA | QLoRA: Efficient Finetuning of Quantized LLMs | Tim Dettmers, Artidoro Pagnoni, Ari Holtzman, Luke Zettlemoyer | 2023 | [arXiv](https://arxiv.org/abs/2305.14314), [GitHub](https://github.com/artidoro/qlora) | Ajuste eficiente con modelo cuantizado a 4 bits y adaptadores LoRA | Verificado |
| LLaVA | Visual Instruction Tuning | Haotian Liu, Chunyuan Li, Qingyang Wu, Yong Jae Lee | 2023 | [arXiv](https://arxiv.org/abs/2304.08485), [GitHub](https://github.com/haotian-liu/LLaVA), [Proyecto](https://llava-vl.github.io/) | Adaptación de modelos visión-lenguaje mediante instruction tuning multimodal | Verificado |
| LLaMA_Adapter_V2 | LLaMA-Adapter V2: Parameter-Efficient Visual Instruction Model | Peng Gao et al. | 2023 | [arXiv](https://arxiv.org/abs/2304.15010), [GitHub](https://github.com/ZrrSkywalker/LLaMA-Adapter) | Adaptación multimodal eficiente con pocos parámetros entrenables e integración de tokens visuales | Verificado |
| GPTQ | GPTQ: Accurate Post-Training Quantization for Generative Pre-trained Transformers | Elias Frantar, Saleh Ashkboos, Torsten Hoefler, Dan Alistarh | 2022 | [arXiv](https://arxiv.org/abs/2210.17323), [GitHub](https://github.com/IST-DASLab/gptq) | Cuantización post-entrenamiento para reducir memoria e inferencia en modelos generativos grandes | Verificado |
| AWQ | AWQ: Activation-aware Weight Quantization for LLM Compression and Acceleration | Ji Lin et al. | 2023 | [arXiv](https://arxiv.org/abs/2306.00978), [GitHub](https://github.com/mit-han-lab/llm-awq) | Cuantización consciente de activaciones para compresión y aceleración de LLMs y VLMs | Verificado |

#### Papers complementarios orientados al futuro

| Referencia base | Título completo | Autores | Año | Fuente oficial | Uso en el curso | Estado |
|---|---|---|---:|---|---|---|
| Visual_Prompt_Tuning | Visual Prompt Tuning | Menglin Jia, Luming Tang, Bor-Chun Chen, Claire Cardie, Serge Belongie, Bharath Hariharan, Ser-Nam Lim | 2022 | [arXiv](https://arxiv.org/abs/2203.12119) | Prompt tuning visual para adaptar modelos de visión sin ajustar todos los parámetros | Complementario |
| CLIP_Adapter | CLIP-Adapter: Better Vision-Language Models with Feature Adapters | Peng Gao, Shijie Geng, Renrui Zhang, Teli Ma, Rongyao Fang, Yongfeng Zhang, Hongsheng Li, Yu Qiao | 2021 | [arXiv](https://arxiv.org/abs/2110.04544) | Adaptación ligera de CLIP mediante adapters en características visuales o lingüísticas | Complementario |
| Tip_Adapter | Tip-Adapter: Training-free Adaption of CLIP for Few-shot Classification | Renrui Zhang et al. | 2022 | [arXiv](https://arxiv.org/abs/2207.09519), [GitHub](https://github.com/gaopengcuhk/Tip-Adapter) | Adaptación few-shot de CLIP mediante cache key-value y opción de ajuste ligero | Complementario |
| MaPLe | MaPLe: Multi-modal Prompt Learning | Muhammad Uzair Khattak, Hanoona Rasheed, Muhammad Maaz, Salman Khan, Fahad Shahbaz Khan | 2022 | [arXiv](https://arxiv.org/abs/2210.03117), [GitHub](https://github.com/muzairkhattak/multimodal-prompt-learning) | Prompt learning simultáneo en ramas visual y textual para mejorar alineamiento | Complementario |
| DoRA | DoRA: Weight-Decomposed Low-Rank Adaptation | Shih-Yang Liu et al. | 2024 | [arXiv](https://arxiv.org/abs/2402.09353), [GitHub](https://github.com/NVlabs/DoRA) | Variante moderna de LoRA que separa magnitud y dirección para mejorar capacidad de adaptación | Complementario |
| PiSSA | PiSSA: Principal Singular Values and Singular Vectors Adaptation of Large Language Models | Fanxu Meng, Zhaohui Wang, Muhan Zhang | 2024 | [arXiv](https://arxiv.org/abs/2404.02948) | Inicialización PEFT basada en componentes principales para convergencia más rápida y compatibilidad con cuantización | Complementario |
| MoRA | MoRA: High-Rank Updating for Parameter-Efficient Fine-Tuning | Ting Jiang et al. | 2024 | [arXiv](https://arxiv.org/abs/2405.12130) | Alternativa a LoRA con actualización de mayor rango manteniendo eficiencia paramétrica | Complementario |
| GaLore | GaLore: Memory-Efficient LLM Training by Gradient Low-Rank Projection | Jiawei Zhao, Zhenyu Zhang, Beidi Chen, Zhangyang Wang, Anima Anandkumar, Yuandong Tian | 2024 | [arXiv](https://arxiv.org/abs/2403.03507), [GitHub](https://github.com/jiaweizzhao/GaLore) | Entrenamiento y fine-tuning con menor memoria mediante proyección de gradientes de bajo rango | Complementario |
| LoftQ | LoftQ: LoRA-Fine-Tuning-Aware Quantization for Large Language Models | Yixiao Li et al. | 2023 | [arXiv](https://arxiv.org/abs/2310.08659), [GitHub](https://github.com/yxli2123/LoftQ) | Integración entre cuantización e inicialización LoRA para reducir brecha frente a modelos full precision | Complementario |
| QuaRot | QuaRot: Outlier-Free 4-Bit Inference in Rotated LLMs | Saleh Ashkboos et al. | 2024 | [arXiv](https://arxiv.org/abs/2404.00456), [GitHub](https://github.com/spcl/QuaRot) | Cuantización de pesos, activaciones y KV cache mediante rotaciones para inferencia eficiente | Complementario |
| SpinQuant | SpinQuant: LLM Quantization with Learned Rotations | Zechun Liu et al. | 2024 | [arXiv](https://arxiv.org/abs/2405.16406) | Cuantización con rotaciones aprendidas para reducir errores en pesos, activaciones y KV cache | Complementario |
| BitNet_CPP | 1-bit AI Infra: Part 1.1, Fast and Lossless BitNet b1.58 Inference on CPUs | Jinheng Wang et al. | 2024 | [arXiv](https://arxiv.org/abs/2410.16144), [GitHub](https://github.com/microsoft/BitNet) | Línea futura de inferencia local y eficiente con modelos ternarios tipo BitNet b1.58 | Exploratorio |
| OpenVLA | OpenVLA: An Open-Source Vision-Language-Action Model | Moo Jin Kim et al. | 2024 | [arXiv](https://arxiv.org/abs/2406.09246) | Caso futuro de adaptación eficiente en modelos visión-lenguaje-acción con LoRA y cuantización | Exploratorio |

#### Nota para estudiantes

Antes de citar un trabajo, se debe verificar la referencia completa en la fuente oficial. Esta lista sirve como guía de lectura del curso y no reemplaza una ficha bibliográfica formal.

La Semana 11 no se debe interpretar como una semana de entrenamiento masivo. El objetivo es comprender cuándo conviene adaptar un modelo, qué parte del modelo se modifica, cuánto cuesta, qué se gana y qué riesgos metodológicos aparecen.

#### Ruta sugerida de lectura

1. Leer Adapters para entender la idea base de módulos pequeños con modelo congelado.
2. Leer Prefix-Tuning y Prompt Tuning para estudiar prompts continuos entrenables.
3. Leer LoRA para comprender adaptación de bajo rango.
4. Leer QLoRA para conectar LoRA con cuantización y reducción de memoria.
5. Leer LLaVA y LLaMA-Adapter V2 para ver adaptación multimodal eficiente.
6. Leer GPTQ y AWQ para entender cuantización post-entrenamiento e inferencia eficiente.
7. Leer Visual Prompt Tuning, CLIP-Adapter, Tip-Adapter y MaPLe para estudiar adaptación de modelos visión-lenguaje.
8. Leer DoRA, PiSSA, MoRA y GaLore para comparar líneas modernas de PEFT y entrenamiento eficiente.
9. Leer LoftQ, QuaRot, SpinQuant y BitNet CPP para discutir cuantización avanzada, KV cache y despliegue local.
10. Leer OpenVLA como puente hacia adaptación eficiente de sistemas visión-lenguaje-acción.


#### Advertencia metodológica

Una adaptación eficiente no debe evaluarse solo por funcionar en una demo. Debe compararse contra una línea base, reportar configuración, datos, parámetros entrenables, memoria aproximada, costo de inferencia, métricas por tarea y errores representativos.

Una cuantización tampoco debe asumirse inocua. Debe verificarse si cambia respuestas, grounding, sensibilidad a prompts, alucinación o desempeño en subgrupos de ejemplos.
