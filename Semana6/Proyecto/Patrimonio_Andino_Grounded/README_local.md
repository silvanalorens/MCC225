### **Patrimonio Andino Grounded**

Proyecto de trabajo para **captioning, generación condicionada y atención visual-semántica** con foco en **Open Khipu** y **Paracas**, adaptado para ejecutarse dentro del entorno Docker del curso en Linux.

#### **Ubicación final recomendada**

Esta versión está pensada para copiarse exactamente en:

```text
/workspace/Semana6/Proyecto/Patrimonio_Andino_Grounded/
```

y quedará con la jerarquía esperada:

```text
MCC225/
└── Semana6/
    └── Proyecto/
        └── Patrimonio_Andino_Grounded/
```

#### **Qué incluye**

- una muestra real pequeña ya normalizada,
- un pipeline reproducible de **recuperación + generación grounded**,
- una ruta opcional con un modelo real de captioning,
- casos comentados en profundidad,
- notebooks `00` a `10` listos para usar y adaptar,
- detección de entorno pensada para `/workspace`,
- documentación específica para Docker/Linux y para la estructura del curso.

#### **Orden recomendado de uso**

1. `notebooks/10_verificacion_entorno_docker_linux.ipynb`
2. `notebooks/07_demo_integrada_y_modelo_real_opcional.ipynb`
3. `notebooks/08_corrida_local_rtx4080_opcional.ipynb` si CUDA está disponible
4. `notebooks/09_casos_comentados_en_profundidad.ipynb`
5. Luego, si quieres, recorre la secuencia completa `00–06`

#### **Qué NO hace esta versión**

- no redistribuye imágenes patrimoniales externas,
- no entrena modelos grandes desde cero,
- no asume que toda imagen técnica y toda foto patrimonial deben producir el mismo tipo de texto.

#### **Arranque rápido**

1. Levanta el contenedor del curso.
2. Abre JupyterLab en `http://localhost:8899/lab`.
3. Ve a `Semana6/Proyecto/Patrimonio_Andino_Grounded/notebooks/`.
4. Ejecuta primero `10_verificacion_entorno_docker_linux.ipynb`.
5. Si el entorno está correcto, continúa con `07_demo_integrada_y_modelo_real_opcional.ipynb`.


#### **Comentarios sobre rutas**

Los notebooks intentan detectar automáticamente la raíz del proyecto. Aun así, esta versión  asume como ruta preferida:

```text
/workspace/Semana6/Proyecto/Patrimonio_Andino_Grounded
```

Si trabajas desde otra ubicación, ajusta `PROJECT_ROOT` o `BASE_DIR` al inicio del cuaderno.
