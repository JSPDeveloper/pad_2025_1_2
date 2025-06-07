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
