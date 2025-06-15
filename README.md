# edu_pad

[![Python](https://img.shields.io/badge/Python-3.9-blue.svg?style=for-the-badge&logo=python&logoColor=yellow)](https://www.python.org/)
[![Docker](https://img.shields.io/badge/Docker-ready-blue.svg?style=for-the-badge&logo=docker&logoColor=white)](https://www.docker.com/)
[![GitHub Actions](https://img.shields.io/badge/CI%2FCD-GitHub%20Actions-blue.svg?style=for-the-badge&logo=githubactions&logoColor=white)](https://github.com/features/actions)
[![License](https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge&logo=opensourceinitiative&logoColor=white)](https://opensource.org/licenses/MIT)

## Descripción del Proyecto

`edu_pad` es un proyecto de scraping desarrollado para la IU Digital, enfocado en la extracción y procesamiento de datos web para diversos fines, incluyendo la ingesta de información y la interacción con bases de datos.

Este proyecto está diseñado para ejecutarse en un entorno Dockerizado, lo que garantiza un despliegue consistente y reproducible.

## Características Principales

* **Extracción de Datos Web:** Utiliza las potentes librerías [requests](https://docs.python-requests.org/en/latest/) y [beautifulsoup4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) para realizar scraping de información desde la web de manera eficiente.

    [![requests](https://img.shields.io/badge/requests-2.28.1-brightgreen.svg?style=flat-square&logo=python&logoColor=white)](https://docs.python-requests.org/en/latest/)
    [![beautifulsoup4](https://img.shields.io/badge/beautifulsoup4-4.11.1-brightgreen.svg?style=flat-square&logo=python&logoColor=white)](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
* **Procesamiento de Datos:** Emplea la librería [pandas](https://pandas.pydata.org/) para el manejo y análisis estructurado de datos.

    [![pandas](https://img.shields.io/badge/pandas-1.5.0-brightgreen.svg?style=flat-square&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
* **Persistencia de Datos:** Permite la interacción con bases de datos (como se evidencia en los archivos `database.py` y `mi_base.db`).
* **Dockerizado:** Empaquetado en un contenedor Docker para un despliegue sencillo y consistente en diferentes entornos.
* **Automatización con GitHub Actions:** Integra flujos de trabajo de CI/CD para la construcción y prueba automática del proyecto con cada cambio en el repositorio.

## Estructura del Proyecto
```
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
```
<<<<<<< HEAD

## Requisitos

Para construir y ejecutar este proyecto, necesitas tener instalado:

* [Docker](https://www.docker.com/get-started/)
* [Python 3.9+](https://www.python.org/downloads/) (si vas a ejecutarlo directamente sin Docker, lo cual no es el enfoque principal aquí)

## Instalación y Ejecución

### 1. Clonar el Repositorio

```bash
git clone [https://github.com/JSPDeveloper/pad_2025_1_2.git](https://github.com/JSPDeveloper/pad_2025_1_2.git)
cd pad_2025_1_2
```

### 2. Construir la Imagen Docker
Desde el directorio raíz del proyecto (donde se encuentra el Dockerfile):

```bash
docker build -t edu_pad_image .
```
Esto creará una imagen Docker llamada edu_pad_image.


### 3. Ejecutar el Contenedor Docker
Puedes ejecutar el módulo main_extractor de tu proyecto usando:

```bash
docker run edu_pad_image
```

Si necesitas mapear volúmenes o puertos, ajusta el comando docker run según sea necesario.

# Dependencias
Las principales dependencias del proyecto se gestionan a través de setup.py y se instalan automáticamente durante la construcción de la imagen Docker. Incluyen:

- `pandas`
- `openpyxl`
- `requests`
- `beautifulsoup4`


# Flujos de Trabajo de GitHub Actions
Este proyecto utiliza GitHub Actions para la integración continua (CI/CD). El archivo `.github/workflows/docker.yml` define los pasos para construir y, potencialmente, probar o desplegar la aplicación automáticamente cada vez que se realizan cambios en el repositorio.

Puedes ver el estado de las ejecuciones de CI/CD en la pestaña "Actions" de tu repositorio de GitHub.

# Contribuciones
Si deseas contribuir a este proyecto, por favor, sigue estos pasos:

1.Haz un "fork" del repositorio.

2.Crea una nueva rama (`git checkout -b feature/nueva-funcionalidad`).

3.Realiza tus cambios y asegúrate de que el código sea limpio y comentado.

4.Realiza "commit" de tus cambios (`git commit -m 'feat: Añade nueva funcionalidad'`).

5.Haz "push" atu rama (`git push origin feature/nueva-funcionalidad`).

6.Abre un "Pull Request" describiendo tus cambios.

# Licencia
Este proyecto está bajo la Licencia MIT. Consulta el archivo LICENSE (si existe) para más detalles.

# Contacto

Jeison Stiven Parra Garcia - jeison.parra@est.iudigital.edu.co

Jefferson SanJuan Ortiz - jefferson.sanjuan@est.iudigital.edu.co

---
=======

## Requisitos

Para construir y ejecutar este proyecto, necesitas tener instalado:

* [Docker](https://www.docker.com/get-started/)
* [Python 3.9+](https://www.python.org/downloads/) (si vas a ejecutarlo directamente sin Docker, lo cual no es el enfoque principal aquí)

## Instalación y Ejecución

### 1. Clonar el Repositorio

```bash
git clone [https://github.com/JSPDeveloper/pad_2025_1_2.git](https://github.com/JSPDeveloper/pad_2025_1_2.git)
cd pad_2025_1_2
```

### 2. Construir la Imagen Docker
Desde el directorio raíz del proyecto (donde se encuentra el Dockerfile):

```bash
docker build -t edu_pad_image .
```
Esto creará una imagen Docker llamada edu_pad_image.


### 3. Ejecutar el Contenedor Docker
Puedes ejecutar el módulo main_extractor de tu proyecto usando:

```bash
docker run edu_pad_image
```

Si necesitas mapear volúmenes o puertos, ajusta el comando docker run según sea necesario.

# Dependencias
Las principales dependencias del proyecto se gestionan a través de setup.py y se instalan automáticamente durante la construcción de la imagen Docker. Incluyen:

- `pandas`
- `openpyxl`
- `requests`
- `beautifulsoup4`


# Flujos de Trabajo de GitHub Actions
Este proyecto utiliza GitHub Actions para la integración continua (CI/CD). El archivo `.github/workflows/docker.yml` define los pasos para construir y, potencialmente, probar o desplegar la aplicación automáticamente cada vez que se realizan cambios en el repositorio.

Puedes ver el estado de las ejecuciones de CI/CD en la pestaña "Actions" de tu repositorio de GitHub.

# Contribuciones
Si deseas contribuir a este proyecto, por favor, sigue estos pasos:

1.Haz un "fork" del repositorio.

2.Crea una nueva rama (`git checkout -b feature/nueva-funcionalidad`).

3.Realiza tus cambios y asegúrate de que el código sea limpio y comentado.

4.Realiza "commit" de tus cambios (`git commit -m 'feat: Añade nueva funcionalidad'`).

5.Haz "push" atu rama (`git push origin feature/nueva-funcionalidad`).

6.Abre un "Pull Request" describiendo tus cambios.

# Licencia
Este proyecto está bajo la Licencia MIT. Consulta el archivo LICENSE (si existe) para más detalles.

# Contacto

Jeison Stiven Parra Garcia - jeison.parra@est.iudigital.edu.co

Jefferson SanJuan Ortiz - jefferson.sanjuan@est.iudigital.edu.co

---
>>>>>>> 9f57292a4248aeb673089f6f53ad9f8c3bb09905
