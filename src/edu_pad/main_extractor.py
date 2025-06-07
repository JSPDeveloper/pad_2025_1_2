from src.edu_pad.datawebv2 import DataWeb
import pandas as pd

def main():
    dataweb=DataWeb()
    df = dataweb.obtener_datos()
    # 🔧 Corregir columnas vacías ANTES de pasarlo a la base de datos
    df.columns = [f"col_{i}" if col is None or str(col).strip() == "" else str(col).strip() for i, col in enumerate(df.columns)]
    df.to_csv("src/edu_pad/static/csv/DataWebPremierLeague.csv",index=False,mode="a")

if __name__ == "__main__":
    main() 