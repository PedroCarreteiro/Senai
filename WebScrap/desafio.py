import requests
from bs4 import BeautifulSoup

from WebScrap.arquivo import response
from WebScrap.identificar_acesso_browser import headers

url = "https://www.cnnbrasil.com.br/"

headers = {
    'User-Agent': 'Mozilla/5.0'
}

#<figcaption class="block--manchetes__caption"> <a href="https://www.cnnbrasil.com.br/economia/macroeconomia/lula-assina-isencao-da-conta-de-luz-veja-os-impactos/"> <h3 class="block__news__title">Lula assina medida provisória que amplia isenção da conta de luz; veja impactos</h3></a> </figcaption>
#<h3 class="block__news__title block__news__title--large-item">Ex-comandante da FAB confirma que Freire Gomes ameaçou prender Bolsonaro</h3>

response = requests.get(url, headers=headers)
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'html.parser')

noticias = soup.find_all("figcaption",class_="")

for noticia in noticias:
    titulo = noticia.a.h3['class']
    link = noticia.find('a', class_="block__news__title--large-item--link").text
    print(f"Titulo {titulo} - link {link}")