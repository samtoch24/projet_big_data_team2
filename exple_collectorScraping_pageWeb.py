import os
from urllib.request import urlretrieve, urlopen
from datetime import datetime
from bs4 import BeautifulSoup

data_destination_path = "C:\\wamp64\\www\\projet_big_data_team2\\Docs collecte"


covid_gouv_url = "https://www.data.gouv.fr/fr/datasets/donnees-hospitalieres-relatives-a-lepidemie-de-covid-19"
destination_extracted_covid_csv_path = os.path.join(data_destination_path, 'extracted_covid.csv')

# Download the page
page = urlopen(covid_gouv_url)

# Read the DOM
soup = BeautifulSoup(page, "html.parser")

# Search for the article
h4 = [elt for elt in soup.findAll("h4") if elt.getText().startswith("donnees-hospitalieres-covid19-2")][0]
article = h4.find_parent('article')

# Extract the link
for a in article.findAll('a'):
    if a.getText() == "Télécharger":
        link = a["href"]
print("link", link)

# Download the file from the link
urlretrieve(link, destination_extracted_covid_csv_path)

# Display downloaded file informations
info = os.stat(destination_extracted_covid_csv_path)
print("size (Mo): ", round(info.st_size/1000000, 3))
print("last_update: ", datetime.fromtimestamp(info.st_ctime))

