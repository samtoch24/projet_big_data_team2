import os
from datetime import datetime
from urllib.request import urlretrieve
from urllib.request import urlopen
from bs4 import BeautifulSoup




# telechargement de la page
url = 'https://catalog.data.gov/dataset/march-2020-presidential-primary-final-precinct-results'

# Analyse de la page
page = urlopen(url)
soup = BeautifulSoup(page, "html.parser")

a = [elt for elt in soup.findAll("a") if 'Download' in elt.getText()][0]
li = a.find_parent('li')

div = [elt for elt in li.findAll('div')][0]
a2 = [elt for elt in div.findAll('a') if 'Download' in elt.getText()][0]

link = a2['href']

# telechargement du fichier à partir du lien
urlretrieve(link, 'TLindsey.csv')

