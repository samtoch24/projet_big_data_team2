import datadotworld as dw
import csv
import os.path
from datetime import datetime
from urllib.request import urlretrieve
from urllib.request import urlopen
from bs4 import BeautifulSoup
#Analyse de la page
# telechargement de la page
#
fivethirtyeigh = dw.load_dataset('fivethirtyeight/2020-general-election-forecast'   )

#creation de notre fichier local
if not os.path.isfile('test.csv'):
        f =open('test.csv','w')
        f.close()

with open('test.csv','w') as w:
    relation = csv.writer(w, delimiter=',')
    relation.writerow(fivethirtyeigh.tables['presidential_state_toplines_2020'][0].keys())
    for i in range(len(fivethirtyeigh.tables['presidential_state_toplines_2020'])):
        relation.writerow(fivethirtyeigh.tables['presidential_state_toplines_2020'][i].values())










