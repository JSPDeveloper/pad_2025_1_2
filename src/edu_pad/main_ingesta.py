from database import DataBase
import pandas as pd

def main():
    
    database=DataBase()
    df = pd.read_csv("src/edu_pad/static/csv/DataWebPremierLeague.csv")
    # Corregir columnas vacías ANTES de pasarlo a la base de datos # Capa 3
    df.columns = [f"col_{i}" if col is None or str(col).strip() == "" else str(col).strip() for i, col in enumerate(df.columns)]
    df_db=database.guardar_df(df)
    df_db2=database.obtener_datos() #Capa 3 guadar en base de datos 
    df_db2.to_csv("src/edu_pad/static/csv/data_db.csv",index=False)


if __name__ == "__main__":
    main() 