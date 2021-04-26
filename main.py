
from datetime import datetime
from urllib.request import urlretrieve
from urllib.request import urlopen
from bs4 import BeautifulSoup
#Analyse de la page
# telechargement de la page
#
url= 'https://catalog.data.gov/dataset/campaign-finance-summary-of-third-party-disclosure-forms-regarding-san-francisco-candidate-eb923'
page= urlopen(url)
soup= BeautifulSoup(page,"html.parser")
str="Comma Separated Values File"
a=[elt for elt in soup.findAll("a") if str in elt.getText()][0]
li=a.find_parent('li')

div = [elt for elt in li.findAll('div')][0]
a2 =  [elt for elt in div.findAll('a') if 'Download' in elt.getText()][0]

link=a2['href']

urlretrieve(link,"concours.csv")






#p=[elt for elt in soup.findAll("p") if elt.getText().startswith('&nbsp;')][0]
#print(p.getText())

#a= [elt for elt in soup.findAll("a") if elt.get('title','Comma Separated Values File') ][0]
#link= a['href']
#print("lien : "+link)