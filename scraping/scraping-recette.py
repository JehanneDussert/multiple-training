import requests
from bs4 import BeautifulSoup

url = "https://codeavecjonathan.com/scraping/recette/"

HEADERS = { "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:127.0) Gecko/20100101 Firefox/127.0" }

def get_text_if_not_none(e):
    if e:
        return e.text.strip()
    return None

response = requests.get(url, headers=HEADERS)
response.encoding = response.apparent_encoding

if response.status_code == 200:
    html = response.text

    f = open("recette.html", "w", encoding='utf-8')
    f.write(html)
    f.close()
    
    soup = BeautifulSoup(html, 'html5lib')
    titre = soup.find("h1").text
    print(titre)
    
    description = get_text_if_not_none(soup.find("p", class_="description"))
    print(description)
    
    # Ingrédients
    div_ingredients = soup.find("div", class_="ingredients")
    e_ingredients = div_ingredients.find_all("p")
    
    for e_ingredient in e_ingredients:
        print("INGREDIENT: ", e_ingredient.text)
        
    # Préparation
    table_preparations = soup.find("table", class_="preparation")
    e_preparations = table_preparations.find_all("td", class_="preparation_etape")
    
    for e_preparation in e_preparations:
        print("INGREDIENT: ", e_preparation.text)
    
else:
    print("ERREUR: ", response.status_code)
print("FIN")