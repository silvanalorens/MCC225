### Docker para MCC225 (Windows)

Se utiliza la imagen de Windows del repositorio https://github.com/kapumota/MCC225.git 
- **`Dockerfile` de Windows

- **`mcc225_cpu`**: para usar en **Windows con Docker Desktop** 

A continuación, se extrae de la guía del repositorio del docente, lo reutilizado https://github.com/kapumota/MCC225.git 

#### 1. Estructura

```text
MCC225/
├── Dockerfile
├── requirements-base.txt
├── requirements-opcional.txt
├── Docker-mcc225.md
├── .dockerignore
└── Semana4/
    ├── ProyectoFinal/
        ├── OpenClip-MCC225.ipynb
        ├── XCLIP_PROJECT.ipynb
        ├── Comparativa.pdf
        ├── README.md
    
```

#### 2. Dockerfile

El `Dockerfile` de este proyecto:

- usa `python:3.11-slim`
- copia `requirements-base.txt` y `requirements-opcional.txt`
- instala primero la base y luego, si corresponde, los paquetes opcionales

#### 6. Construcción de imágen
Se eligió la opción 6.2 Build completa CPU

```bash
docker build --no-cache \
  --build-arg TORCH_FLAVOR=cpu \
  --build-arg INSTALL_OPCIONAL=true \
  -t mcc225_cpu .
```
##### 7.1 Windows PowerShell con Docker Desktop (CPU)

```powershell
docker run -it --rm `
  --name mcc225_cpu_container `
  -p 8899:8899 `
  -v "${PWD}:/workspace" `
  mcc225_cpu
```

##### 7.2 Windows CMD con Docker Desktop (CPU)

```bat
docker run -it --rm --name mcc225_cpu_container -p 8899:8899 -v %cd%:/workspace mcc225_cpu
```
#### 8. Abrir JupyterLab

Al iniciar el contenedor, abre en el navegador:

```text
http://localhost:8899/lab
```

Si Jupyter muestra token, cópialo desde los logs del contenedor.

