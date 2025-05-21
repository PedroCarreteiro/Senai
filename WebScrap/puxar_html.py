from bs4 import BeautifulSoup

from WebScrap.arquivo import response

html = response.text

soup = BeautifulSoup(html,'html.parser')
print(soup.prettify())