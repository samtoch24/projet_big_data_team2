import os
from datetime import datetime
from urllib.request import urlretrieve
from urllib.request import  urlopen
from bs4 import BeautifulSoup


# telechargement de la page
url = 'https://catalog.data.gov/dataset/campaign-finance-summary-of-third-party-disclosure-forms-regarding-san-francisco-candidate-eb923'
page = urlopen(url)

# Analyse de la page (Scraping)
soup = BeautifulSoup(page, "html.parser")
h3 = [elt for elt in soup.findAll("h3") if elt.getText().startswith("Downloads & Resources")][0]
section = h3.find_parent('section')
for a in section.findAll('a'):
    if a.getText() == "Download":
        link = a["href"]
        print(link)


