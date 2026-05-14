#!.venv/bin/python

import requests
from bs4 import BeautifulSoup

sity = input("город: ")
prise = input("максималтная цена: ")

content = {
}

custom_headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }

response = requests.get(f"https://m.avito.ru/{sity}/nedvizhimost", headers=custom_headers)

soup = BeautifulSoup(response.text, "html.parser")

res = soup.find("a", class_="styles-module-root-cfrVG styles-module-root_underlineOffset_size-m-ce9r8 styles-module-root_noVisited-U4swI styles-module-root_preset_black-VfJP4")

print(res.text)
