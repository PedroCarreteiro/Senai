import requests
from bs4 import BeautifulSoup

from WebScrap.arquivo import response
from WebScrap.identificar_acesso_browser import headers

url = "https://www.cnnbrasil.com.br/"

headers = {
    'User-Agent': 'Mozilla/5.0'
}

#<figcaption class="block--manchetes__caption"> <a href="https://www.cnnbrasil.com.br/economia/macroeconomia/lula-assina-isencao-da-conta-de-luz-veja-os-impactos/"> <h3 class="block__news__title">Lula assina medida provisória que amplia isenção da conta de luz; veja impactos</h3></a> </figcaption>


response = requests.get(url, headers=headers)
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'html.parser')

noticias = soup.find_all("div",class_="has--thumb")

for noticia in noticias:
    titulo = noticia.h3.a['block__news__title']
    link = noticia.find('a', class_="block--manchetes__image__encapsulator").text
    print(f"Titulo {titulo} - link {link}")