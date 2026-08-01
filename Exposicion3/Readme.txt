README - Clasificación multimodal de deportes utilizando MSR-VTT
https://github.com/silvanalorens/MCC225/tree/main/Exposicion3

DESCRIPCIÓN DEL EXPERIMENTO
===========================

Este proyecto implementa un pipeline multimodal para la clasificación de categorías deportivas utilizando un subconjunto del dataset MSR-VTT.

Cada video fue representado mediante una secuencia de 12 frames debido a restricciones computacionales. Estas representaciones visuales fueron combinadas con información textual generada automáticamente para construir un dataset multimodal.

Se evaluaron dos arquitecturas multimodales:

- VisualBERT
- LXMERT

Los modelos preentrenados fueron utilizados y únicamente se entrenó una capa externa de clasificación para la tarea de reconocimiento deportivo.
DATASET
=======
2 Muestras de entrenamiento y prueba.
Mejora de captions con blip.
Se utilizó un subconjunto deportivo de MSR-VTT con las categorías:

- Basketball
- Soccer
- Swimming
- Tennis
PERTURBACIONES TEMPORALES
==========================

Original:

Uso de los 12 frames originales.

Shuffle:
Sampling-6: 12 frames -> 6 frames


RESULTADOS
==========

Los experimentos realizados mostraron que LXMERT obtuvo el mejor desempeño en la clasificación de deportes, alcanzando una precisión (Accuracy) de 0.8889 en el conjunto de prueba. Además, este modelo mantuvo el mismo rendimiento en los experimentos de perturbación temporal mediante Shuffle y Sampling-6, evidenciando una mayor robustez frente a cambios en el orden y la cantidad de frames utilizados como representación del video. Por su parte, VisualBERT alcanzó una precisión de 0.7778 en el experimento original y conservó dicho rendimiento con la perturbación Shuffle; sin embargo, al reducir la secuencia de 12 a 6 frames mediante Sampling-6, su precisión disminuyó a 0.1667, lo que indica una mayor sensibilidad a la reducción de información visual en comparación con LXMERT.