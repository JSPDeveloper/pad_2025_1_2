import pandas as pd
import requests
from bs4 import BeautifulSoup

class DataWeb:
    def __init__(self):
        self.base_url = "https://www.worldfootball.net/goalgetter/eng-premier-league-{}/"

    def obtener_datos(self):
        all_data = []
        temporadas = self.generar_temporadas(30)

        for temporada in temporadas:
            url = self.base_url.format(temporada)
            print(f"Scrapeando temporada: {temporada}")
            try:
                headers = {'User-Agent': 'Mozilla/5.0'}
                respuesta = requests.get(url, headers=headers)
                if respuesta.status_code != 200:
                    print(f"Error al acceder a {url}")
                    continue

                soup = BeautifulSoup(respuesta.text, 'html.parser')
                table = soup.find("table", {"class": "standard_tabelle"})
                if not table:
                    print(f"No se encontró la tabla en {url}")
                    continue

                # Obtener encabezados, incluyendo vacíos
                th_elements = table.find("tr").find_all("th")
                namecolumns = []
                ignore_counter = 1
                for th in th_elements:
                    header = th.text.strip()
                    if not header:
                        header = f"Ignore{ignore_counter}"
                        ignore_counter += 1
                    elif header in ['#', 'Pos.']:
                        header = 'Number'
                    namecolumns.append(header)

                # Extraer filas
                rows = []
                position_counter = 1
                for tr in table.find_all("tr")[1:]:
                    columns = [td.text.strip() for td in tr.find_all("td")]
                    if columns and len(columns) == len(namecolumns):
                        columns[0] = str(position_counter)
                        position_counter += 1
                        row_dict = dict(zip(namecolumns, columns))

                        # Eliminar columnas ignoradas
                        for key in list(row_dict.keys()):
                            if key.startswith("Ignore"):
                                del row_dict[key]

                        row_dict["Temporada"] = temporada
                        rows.append(row_dict)

                all_data.extend(rows)

            except Exception as e:
                print(f"Error scrapeando {temporada}: {e}")

        # Crear DataFrame y limpiar
        df = pd.DataFrame(all_data)

        # Limpieza adicional
        if 'Team' in df.columns:
            df['Team'] = df['Team'].str.replace('\n', ' / ')
            df['Team'] = df['Team'].str.replace(r'\s+', ' ', regex=True).str.strip()

        if 'Number' in df.columns:
            df['Number'] = pd.to_numeric(df['Number'], errors='coerce').fillna(0).astype(int)

        # Guardar
        output_file = "DataWebPremierLeague_Ultimas10.xlsx"
        df.to_excel(output_file, index=False)
        print("***********************************************************************************")
        print("Datos Obtenidos de todas las temporadas")
        print("***********************************************************************************")
        print(df.head())
        print(f"Datos guardados exitosamente en: {output_file}")
        return df

    def generar_temporadas(self, cantidad):
        temporadas = []
        actual = 2024  # o podrías usar datetime.datetime.now().year
        for i in range(cantidad):
            start = actual - i
            end = start + 1
            temporadas.append(f"{start}-{end}")
        return temporadas[::-1]  # para que aparezcan de más antigua a reciente

# Ejecutar
# dw = DataWeb()
# df = dw.obtener_datos()
