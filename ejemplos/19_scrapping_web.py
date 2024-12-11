# Compra el libro en:
# www.ellibrodepython.com

# Instrucciones:
# 1. Instala dependencias: pip install requests beautifulsoup4 lxml
# 2. Ejecuta el script: python 19_scrapping_web.py

import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/Python_(programming_language)"
tabla = {}

try:
    response = requests.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'lxml')

    infobox = soup.find('table', class_='infobox vevent')
    if infobox:
        tabla = {
            fila.find('th').get_text(strip=True): fila.find('td').get_text(strip=True)
            for fila in infobox.find_all('tr')
            if fila.find('th') and fila.find('td')
        }

except requests.exceptions.RequestException as e:
    print(f"Error: {e}")

print(tabla["Developer"])
# Python Software Foundation