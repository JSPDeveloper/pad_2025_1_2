# edu_pad

![Python](https://img.shields.io/badge/Python-3.9-blue.svg)
![Docker](https://img.shields.io/badge/Docker-ready-blue.svg)
![GitHub Actions](https://img.shields.io/badge/CI%2FCD-GitHub%20Actions-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg) ## Descripción del Proyecto

`edu_pad` es un proyecto de scraping desarrollado para la IU Digital. Su objetivo principal es la extracción y procesamiento de datos web para diversos fines, incluyendo la ingesta de información y la interacción con bases de datos.

Este proyecto está diseñado para ejecutarse en un entorno Dockerizado, lo que garantiza un despliegue consistente y reproducible.

## Características

* **Extracción de Datos Web:** Utiliza librerías como `requests` y `beautifulsoup4` para realizar scraping de información desde la web.
* **Procesamiento de Datos:** Incorpora `pandas` para el manejo y análisis de datos.
* **Persistencia de Datos:** Interacción con bases de datos (evidenciado por `database.py` y `mi_base.db`).
* **Dockerizado:** Empaquetado en un contenedor Docker para un despliegue sencillo y consistente.
* **Automatización con GitHub Actions:** Incluye flujos de trabajo de CI/CD para la construcción y prueba automática del proyecto.

## Estructura del Proyecto

La estructura principal del proyecto es la siguiente:

Aquí tienes un borrador de un archivo README para tu repositorio de GitHub, basado en la información que me has proporcionado (estructura del proyecto, Dockerfile y setup.py):

Markdown

# edu_pad

![Python](https://img.shields.io/badge/Python-3.9-blue.svg)
![Docker](https://img.shields.io/badge/Docker-ready-blue.svg)
![GitHub Actions](https://img.shields.io/badge/CI%2FCD-GitHub%20Actions-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg) ## Descripción del Proyecto

`edu_pad` es un proyecto de scraping desarrollado para la IU Digital. Su objetivo principal es la extracción y procesamiento de datos web para diversos fines, incluyendo la ingesta de información y la interacción con bases de datos.

Este proyecto está diseñado para ejecutarse en un entorno Dockerizado, lo que garantiza un despliegue consistente y reproducible.

## Características

* **Extracción de Datos Web:** Utiliza librerías como `requests` y `beautifulsoup4` para realizar scraping de información desde la web.
* **Procesamiento de Datos:** Incorpora `pandas` para el manejo y análisis de datos.
* **Persistencia de Datos:** Interacción con bases de datos (evidenciado por `database.py` y `mi_base.db`).
* **Dockerizado:** Empaquetado en un contenedor Docker para un despliegue sencillo y consistente.
* **Automatización con GitHub Actions:** Incluye flujos de trabajo de CI/CD para la construcción y prueba automática del proyecto.

## Estructura del Proyecto

La estructura principal del proyecto es la siguiente:

.
├── .github/
│   └── workflows/          # Configuración de GitHub Actions (ej: docker.yml)
├── src/
│   └── edu_pad/            # Paquete principal del proyecto
│       ├── init.py     # Archivo de inicialización del paquete
│       ├── database.py     # Módulo para la interacción con la base de datos
│       ├── dataweb.py      # Módulo(s) relacionado(s) con la extracción de datos web
│       ├── main_extractor.py # Punto de entrada principal para la extracción
│       ├── main_ingesta.py   # Punto de entrada para la ingesta de datos
│       └── main.py         # Otros módulos principales
│       └── static/         # Recursos estáticos (csv, db)
├── Dockerfile              # Definición para construir la imagen Docker
├── setup.py                # Configuración de empaquetado del proyecto Python
├── requirements.txt        # (Recomendado) Lista de dependencias del proyecto
└── README.md               # Este archivo
└── (otros archivos relevantes)

## Requisitos

Para construir y ejecutar este proyecto, necesitas tener instalado:

* [**Docker**](https://www.docker.com/get-started/)
* [**Python 3.9+**](https://www.python.org/downloads/) (si vas a ejecutarlo directamente sin Docker, lo cual no es el enfoque principal aquí)

## Instalación y Ejecución

### 1. Clonar el Repositorio

```bash
git clone [https://github.com/JSPDeveloper/pad_2025_1_2.git](https://github.com/JSPDeveloper/pad_2025_1_2.git)
cd pad_2025_1_2

Aquí tienes un borrador de un archivo README para tu repositorio de GitHub, basado en la información que me has proporcionado (estructura del proyecto, Dockerfile y setup.py):

Markdown

# edu_pad

![Python](https://img.shields.io/badge/Python-3.9-blue.svg)
![Docker](https://img.shields.io/badge/Docker-ready-blue.svg)
![GitHub Actions](https://img.shields.io/badge/CI%2FCD-GitHub%20Actions-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg) ## Descripción del Proyecto

`edu_pad` es un proyecto de scraping desarrollado para la IU Digital. Su objetivo principal es la extracción y procesamiento de datos web para diversos fines, incluyendo la ingesta de información y la interacción con bases de datos.

Este proyecto está diseñado para ejecutarse en un entorno Dockerizado, lo que garantiza un despliegue consistente y reproducible.

## Características

* **Extracción de Datos Web:** Utiliza librerías como `requests` y `beautifulsoup4` para realizar scraping de información desde la web.
* **Procesamiento de Datos:** Incorpora `pandas` para el manejo y análisis de datos.
* **Persistencia de Datos:** Interacción con bases de datos (evidenciado por `database.py` y `mi_base.db`).
* **Dockerizado:** Empaquetado en un contenedor Docker para un despliegue sencillo y consistente.
* **Automatización con GitHub Actions:** Incluye flujos de trabajo de CI/CD para la construcción y prueba automática del proyecto.

## Estructura del Proyecto

La estructura principal del proyecto es la siguiente:

.
├── .github/
│   └── workflows/          # Configuración de GitHub Actions (ej: docker.yml)
├── src/
│   └── edu_pad/            # Paquete principal del proyecto
│       ├── init.py     # Archivo de inicialización del paquete
│       ├── database.py     # Módulo para la interacción con la base de datos
│       ├── dataweb.py      # Módulo(s) relacionado(s) con la extracción de datos web
│       ├── main_extractor.py # Punto de entrada principal para la extracción
│       ├── main_ingesta.py   # Punto de entrada para la ingesta de datos
│       └── main.py         # Otros módulos principales
│       └── static/         # Recursos estáticos (csv, db)
├── Dockerfile              # Definición para construir la imagen Docker
├── setup.py                # Configuración de empaquetado del proyecto Python
├── requirements.txt        # (Recomendado) Lista de dependencias del proyecto
└── README.md               # Este archivo
└── (otros archivos relevantes)


## Requisitos

Para construir y ejecutar este proyecto, necesitas tener instalado:

* [**Docker**](https://www.docker.com/get-started/)
* [**Python 3.9+**](https://www.python.org/downloads/) (si vas a ejecutarlo directamente sin Docker, lo cual no es el enfoque principal aquí)

## Instalación y Ejecución

### 1. Clonar el Repositorio

```bash
git clone [https://github.com/JSPDeveloper/pad_2025_1_2.git](https://github.com/JSPDeveloper/pad_2025_1_2.git)
cd pad_2025_1_2
2. Construir la Imagen Docker
Desde el directorio raíz del proyecto (donde se encuentra Dockerfile):
docker build -t edu_pad_image .
