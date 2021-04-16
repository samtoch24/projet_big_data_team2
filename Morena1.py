import os
from datetime import datetime
from urllib.request import urlretrieve
from urllib.request import urlopen
from bs4 import BeautifulSoup


# Destination file
data_destination_path = "C:\\wamp64\\www\\projet_big_data_team2\\Docs collecte"
destination_extracted_covid_pdf_path = os.path.join(data_destination_path, 'USA_Elections_InBrief_French.pdf')

# telechargement de la page
url = 'https://search.usa.gov/search?utf8=%E2%9C%93&affiliate=usagov&query=elections+pr%C3%A9sidentielles'

# Analyse de la page
page = urlopen(url)
soup = BeautifulSoup(page, "html.parser")

h4 = [elt for elt in soup.findAll("h4") if 'ÉLECTIONS' in elt.getText()][0]
a = [elt for elt in h4.findAll('a') if 'ÉLECTIONS' in elt.getText()][0]
link = a['href']

# telechargement du fichier à partir du lien
urlretrieve(link, destination_extracted_covid_pdf_path)

# Display downloaded file informations
info = os.stat(destination_extracted_covid_pdf_path)
print("size (Mo): ", round(info.st_size/1000000, 3))
print("last_update: ", datetime.fromtimestamp(info.st_ctime))

