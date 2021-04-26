import datadotworld as dw
import csv
import os.path

#All_files = dw.load_dataset('fivethirtyeight/2020-general-election-forecast', 'data')
#my_file = All_files.raw_data['presidential_state_toplines_2020']
#result = dw.query( 'fivethirtyeight/2020-general-election-forecast' ,  'SELECT * FROM presidential_state_toplines_2020')
#print(result)
#print(len(All_files.tables['presidential_state_toplines_2020']))
#my_file = All_files.tables['presidential_state_toplines_2020'][0]
#print(my_file.value())

#with dw.open_remote_file('fivethirtyeight/2020-general-election-forecast', 'presidential_state_toplines_2020.csv') as w:
 #   my_file.to_csv(w, index=False)

#https://data.world/fivethirtyeight/2020-general-election-forecast/workspace/file?filename=presidential_state_toplines_2020.csv


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













