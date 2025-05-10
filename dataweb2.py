import requests
from bs4 import BeautifulSoup

url = "https://www.worldfootball.net/goalgetter/eng-premier-league-2024-2025/"
headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')

# Buscar la tabla principal (hay varias, usamos la 1ra con class="standard_tabelle")
table = soup.find("table", {"class": "standard_tabelle"})
print (table)

# Encabezados (tienen etiquetas <th>)
headers = [th.text.strip() for th in table.find_all("th")]
print("Encabezados:", headers)

# Filas de datos
data = []
for row in table.find_all("tr")[1:]:
    cols = [td.text.strip() for td in row.find_all("td")]
    if cols:
        data.append(dict(zip(headers, cols)))

# Mostrar resultados
print("\nPrimeros 5 registros:")
for r in data[:5]:
    print(r)
