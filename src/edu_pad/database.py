import pandas as pd
import sqlite3
import os
from datetime import date

class DataBase:
    def __init__(self):
        self.rutadb = "src/edu_pad/static/db/dbAnalisisFutbol.db"

    def guardar_df(self, df=pd.DataFrame()):
        df = df.copy()
        try:
            conn = sqlite3.connect(self.rutadb)
            fecha_actual = date.today() 
            df["fecha_create"] = fecha_actual            
            df["fecha_update"] = fecha_actual
            df.to_sql("dbAnalisisFutbol", conn, if_exists='replace', index=False)
            conn.close()
            print("***********************************************************************************")
            print("Datos guardados exitosamente")
            print("***********************************************************************************")
            print("Se guardó el DataFrame en base de datos, cantidad de registros {}".format(df.shape))                          
        except Exception as errores:
            print(f"Error al guardar el df en base de datos: {errores}")

    def obtener_datos(self, nombre_tabla="dbAnalisisFutbol"):
        try:
            conn = sqlite3.connect(self.rutadb)
            consulta = "SELECT * FROM {}".format(nombre_tabla)
            df = pd.read_sql_query(consulta, conn)
            conn.close()
            print("***********************************************************************************")
            print("Se obtuvieron los datos de la BD")
            print("***********************************************************************************")
            print("Base de datos: cantidad de registros {}".format(df.shape))  
            return df
        except Exception as errores:
            print(f"Error al obtener los datos de la tabla: {errores}")    
            return pd.DataFrame()
