import sqlite3
import pandas as pd
from datetime import date
import os

# Simular tu ruta
ruta_relativa = "src/edu_pad/static/db/dbAnalisisFutbol.db"
ruta_absoluta = os.path.abspath(ruta_relativa)
print(f"Ruta absoluta: {ruta_absoluta}")

# Crear un DataFrame de prueba
df = pd.DataFrame({
    "jugador": ["Messi", "Cristiano"],
    "goles": [30, 28],
})
fecha_actual = date.today()
df["fecha_create"] = fecha_actual
df["fecha_update"] = fecha_actual

# Conexión y guardado
conn = sqlite3.connect(ruta_absoluta)
print("Guardando df...")
df.to_sql("dbAnalisisFutbol", conn, if_exists='replace', index=False)

# Verificar tabla creada
cursor = conn.cursor()
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tablas = [row[0] for row in cursor.fetchall()]
print(f"Tablas en la BD: {tablas}")

# Leer de nuevo
df_leido = pd.read_sql_query("SELECT * FROM dbAnalisisFutbol", conn)
print("Contenido de la tabla:")
print(df_leido)

conn.close()
