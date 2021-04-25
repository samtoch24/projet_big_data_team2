import os
from urllib.request import urlretrieve, urlopen
from datetime import datetime
from bs4 import BeautifulSoup
import ssl

from flask import render_template


def vote_tendancy_latest_download():
    # Destination file
    data_destination_path = "C:/wamp64/www/projet_big_data_team2/Docs coll"
    destination_extracted_votes_csv_path = os.path.join(data_destination_path, 'presidential-primary-final-precinct-results.csv')
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
    urlretrieve(link, destination_extracted_votes_csv_path)
    # Display downloaded file informations
    info = os.stat(destination_extracted_votes_csv_path)

    #return {render_template("<html><head><title>x</title></head><body><h3>path : ", destination_extracted_votes_csv_path, "size : ", round(info.st_size / 1000000, 3), "last_update : ", datetime.fromtimestamp(info.st_ctime).strftime('%Y - % m - % d % H: % M: % S'), "</h3></body></html>")}
    #return {"path": destination_extracted_votes_csv_path, "size": round(info.st_size / 1000000, 3),
            #"last_update": datetime.fromtimestamp(info.st_ctime).strftime('%Y - % m - % d % H: % M: % S')}
    return {
        "path": destination_extracted_votes_csv_path,
        "size": round(info.st_size / 1000000, 3),
        "last_update": datetime.fromtimestamp(info.st_ctime).strftime('%Y-%m-%d %H:%M:%S')}