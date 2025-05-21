from bs4 import BeautifulSoup

from WebScrap.arquivo import response

import requests

url = "https://g1.globo.com/"
response = requests.get(url)
html = response.text

soup = BeautifulSoup(html,'html.parser')
print(soup.prettify())

titulos = soup.find_all('article')

for titulo in titulos:
    print(titulo)