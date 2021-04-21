import os
from urllib.request import urlretrieve, urlopen
from datetime import datetime
from bs4 import BeautifulSoup
import ssl


def popularity_latest_download():
    # set parameters
    data_destination_path = "C:\\wamp64\\www\\projet_big_data_team2\\Docs coll"
    pop_gouv_url = "https://catalog.data.gov/dataset/campaign-finance-summary-of-third-party-disclosure-forms-regarding-san-francisco-candidate-eb923"
    destination_extracted_pop_csv_path = os.path.join(data_destination_path, 'extracted_popularity.csv')

    # create an https context
    ssl._create_default_https_context = ssl._create_unverified_context

    # get the page
    page = urlopen(pop_gouv_url)

    # read the DOM
    soup = BeautifulSoup(page, "html.parser")

    # search for the article
    a = [elt for elt in soup.findAll("a") if 'Download' in elt.getText()][0]
    li = a.find_parent('li')



    # extract the link
    div = [elt for elt in li.findAll('div')][0]
    a2 = [elt for elt in div.findAll('a') if 'Download' in elt.getText()][0]
    link = a2['href']

    # download the file from the link
    urlretrieve(link, destination_extracted_pop_csv_path)

    # return file infos as JSON
    info = os.stat(destination_extracted_pop_csv_path)
    return {"path": destination_extracted_pop_csv_path, "size": round(info.st_size / 1000000, 3), "last_update": datetime.fromtimestamp(info.st_ctime).strftime('%Y - % m - % d % H: % M: % S')}
