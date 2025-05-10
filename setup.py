from setuptools import setup, find_packages

setup (
    name="edu_pad",
    version="0.0.1",
    #version componente.version funcionalidad.version cambio
    author="Jeison Stiven Parra Garcia- Jefferson SanJuan Ortiz",
    author_email="jeison.parra@est.iudigital.edu.co - ",
    description="Proyecto Scraping para IU Digital",
    py_modules=["actividad1","actividad2"],
    install_requires=[
        "pandas",
        "openpyxl",
        "requests",
        "beautifulsoup4"   
    ]
)
