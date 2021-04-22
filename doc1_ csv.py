import os
from datetime import datetime
from urllib.request import urlretrieve
from urllib.request import urlopen
from bs4 import BeautifulSoup


# Destination file
data_destination_path = "C:\\wamp64\\www\\projet_big_data_team2\\Docs coll"
destination_extracted_popularity_csv_path = os.path.join(data_destination_path, 'concours.csv')

# telechargement de la page
url = 'https://catalog.data.gov/dataset/campaign-finance-summary-of-third-party-disclosure-forms-regarding-san-francisco-candidate-eb923'

# Analyse de la page
page = urlopen(url)
soup = BeautifulSoup(page, "html.parser")

a = [elt for elt in soup.findAll("a") if 'Download' in elt.getText()][0]
li = a.find_parent('li')

div = [elt for elt in li.findAll('div')][0]
a2 = [elt for elt in div.findAll('a') if 'Download' in elt.getText()][0]

link = a2['href']

# telechargement du fichier à partir du lien
urlretrieve(link, destination_extracted_popularity_csv_path)

# Display downloaded file informations
info = os.stat(destination_extracted_popularity_csv_path)
print("size (Mo): ", round(info.st_size/1000000, 3))
print("last_update: ", datetime.fromtimestamp(info.st_ctime))

