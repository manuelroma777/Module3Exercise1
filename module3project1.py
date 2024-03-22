import requests
import inflection
from bs4 import BeautifulSoup

# URL del sitio web
url = "https://www.dailysmarty.com/topics/python"

# Realizar la solicitud GET
response = requests.get(url)

# Parsear el contenido HTML
soup = BeautifulSoup(response.text, "html.parser")

# Encontrar todos los enlaces de los artículos
article_links = soup.find_all("a", class_="featured-post-card__title-link")

# Lista para almacenar los títulos
titles = []

# Recorrer los enlaces y obtener los títulos
for link in article_links:
    article_url = link["href"]
    response = requests.get(article_url)
    article_soup = BeautifulSoup(response.text, "html.parser")
    article_title = article_soup.find("h1", class_="post-content__title").text.strip()
    # Convertir el título a un formato normal sin signos "-"
    normalized_title = inflection.titleize(article_title.replace("-", " "))
    titles.append(normalized_title)

# Imprimir los títulos
print("Main Titles: ")
for title in titles:
    print("- ", title)
