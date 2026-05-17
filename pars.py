#!.venv/bin/python

import requests
from bs4 import BeautifulSoup

сity = input("город: ")
priсe = input("максималтная цена: ")

content = {
}

custom_headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }

response = requests.get(f"https://m.avito.ru/{сity}/nedvizhimost", headers=custom_headers)

print("iva-item" in response.text)
print(response.status_code)

soup = BeautifulSoup(response.text, "html.parser")

for r in soup.find_all("div", class_="body-root-YwlPk"):
    print("t")
    
    name = r.find("a", class_="styles-module-root-cfrVG styles-module-root_underlineOffset_size-m-ce9r8 styles-module-root_noVisited-U4swI styles-module-root_preset_black-VfJP4")
    print(name.text)
    print(f"https://www.avito.ru{name["href"]}")

with open("test.txt", "w", encoding="utf-8" ) as f:
    f.write(soup.prettify())
