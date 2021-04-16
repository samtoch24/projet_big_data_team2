from urllib.request import urlopen
from bs4 import BeautifulSoup
from collections import Counter
import re


# telechargement de la page
url = 'https://twitter.com/Elections2020_'
Elections2020_Account = urlopen(url)

# Analyse de la page (Scraping)
soup = BeautifulSoup(Elections2020_Account, features="lxml")
s = soup.find("<html>")
print(s)
