import requests
from bs4 import BeautifulSoup

from WebScrap.arquivo import response
from WebScrap.identificar_acesso_browser import headers

url = "http://books.toscrape.com"

headers = {
    'User-Agent': 'Mozilla/5.0'
}

response = requests.get(url, headers=headers)
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'html.parser')

livros = soup.find_all("article",class_="product_pod")

for livro in livros:
    titulo = livro.h3.a['title']
    preco = livro.find('p', class_="price_color").text
    print(f"Nome {titulo} - Preco {preco}")
