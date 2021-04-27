from urllib.request import urlretrieve
from urllib.request import urlopen
from bs4 import BeautifulSoup


def popularity_on_media_pdf():
    # telechargement de la page
    url = 'https://search.usa.gov/search?utf8=%E2%9C%93&affiliate=usagov&query=elections+pr%C3%A9sidentielles'

    # Analyse de la page
    page = urlopen(url)
    soup = BeautifulSoup(page, "html.parser")

    h4 = [elt for elt in soup.findAll("h4") if 'ÉLECTIONS' in elt.getText()][0]
    a = [elt for elt in h4.findAll('a') if 'ÉLECTIONS' in elt.getText()][0]
    link = a['href']

    # telechargement du fichier à partir du lien
    urlretrieve(link, 'file/morenam.pdf')


