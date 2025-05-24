from dataweb import DataWeb
import pandas as pd

def main_1():
    dataweb=DataWeb()
    df = dataweb.obtener_datos()
    # Corregir columnas vacías ANTES de pasarlo a la base de datos # Capa 3
    df.columns = [f"col_{i}" if col is None or str(col).strip() == "" else str(col).strip() for i, col in enumerate(df.columns)]
    df.to_csv("src/edu_pad/static/csv/data_extractor.csv",index=False)


if __name__ == "__main__":
    main_1() 