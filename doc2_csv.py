import datadotworld as dw
import csv
import os.path


# telechargement du dataset
dataset = dw.load_dataset('fivethirtyeight/2020-general-election-forecast'   )

# creation de notre fichier en local
if not os.path.isfile('presidential_state_toplines_2020.csv'):
        f =open('presidential_state_toplines_2020.csv','w')
        f.close()

with open('presidential_state_toplines_2020.csv','w') as w:
    relation = csv.writer(w, delimiter=',')
    relation.writerow(dataset.tables['presidential_state_toplines_2020'][0].keys())
    for i in range(len(dataset.tables['presidential_state_toplines_2020'])):
        relation.writerow(dataset.tables['presidential_state_toplines_2020'][i].values())










