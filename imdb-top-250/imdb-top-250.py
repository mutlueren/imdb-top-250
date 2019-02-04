#you must install the 'requests' and 'bs4' tools on your cpu

import requests

from bs4 import BeautifulSoup

url = "https://www.imdb.com/chart/top"

r = requests.get(url)

soup = BeautifulSoup(r.content,"html.parser")


gelen_veri = soup.find_all("table",{"class":"chart full-width"})

filmtablosu = (gelen_veri[0].contents)[len(gelen_veri[0].contents)-2]

filmtablosu = filmtablosu.find_all("tr")

for film in filmtablosu:
    basliklar = film.find_all("td",{"class":"titleColumn"})
    filmadi = basliklar[0].text
    print(filmadi)
    print("********************************")

