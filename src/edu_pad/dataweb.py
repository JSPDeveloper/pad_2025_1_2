import pandas as pd
import requests
from bs4 import BeautifulSoup
import datetime

class DataWeb:
    def __init__(self):
        self.url="https://www.worldfootball.net/goalgetter/eng-premier-league-2024-2025/"
       
    def obtener_datos(self):
        try:
            #URL Cabeceras
            headers = {
                        'User-Agent': 'Mozilla/5.0'
            }
            respuesta=requests.get(self.url,headers=headers)
            if respuesta.status_code !=200:
               
                print("La URL saco error, no respondio o no existe")
                print(respuesta.text)
            soup=BeautifulSoup(respuesta.text,'html.parser')
                
            table = soup.find("table", {"class": "standard_tabelle"})
       
            
            # Encabezados (tienen etiquetas <th>)
               
            namecolumns = [th.text.strip() for th in table.find_all("th")]
            #print("Encabezados:", namecolumns)
            
            # Renombrar campo si existe
            namecolumns = ['Number' if h in ['#', 'Pos.'] else h for h in namecolumns]
            
            # Filas de datos
            rows = []
            position_counter = 1  # Contador para la posición secuencial
            for tr in table.find_all("tr")[1:]:
                columns = [td.text.strip() for td in tr.find_all("td")]
                if columns:
                    # Asignar número secuencial a la posición
                    columns[0] = str(position_counter)  # Reemplaza la posición con el número secuencial
                    position_counter += 1  # Incrementa el contador de posición
                    
                    rows.append(dict(zip(namecolumns, columns)))
            
            # Mostrar resultados
            # print("\nPrimeros 5 registros:")
            # for r in rows[:20]:
            #     print(r)

            #Creamos un DataFrame
            df=pd.DataFrame(rows,columns=namecolumns)
            
            # Reemplazamos los  saltos de línea por ' / ' en la columna de Team (ajusta el nombre si es diferente)
            if 'Team' in df.columns:
                df['Team'] = df['Team'].str.replace('\n', ' / ')

            # Aseguramos que la columna de número sea entera
            df['Number'] = df['Number'].astype(int)

            
            df['Team'] = df['Team'].str.replace(r'\s+', ' ', regex=True).str.strip()

            #Guardo la información en un Excel
            df.to_excel("DataWebPremierLeague.xlsx")

            print("***********************************************************************************")
            print("Datos Obtenidos")
            print("***********************************************************************************")
            print(df.head())
            return df
        except Exception as err:
            print ("Error en la función obtener datos")
            df = pd.DataFrame()

           
# dw=DataWeb()
# dw.obtener_datos()
# print(dw.url)