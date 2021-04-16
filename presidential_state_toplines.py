
import os
import pandas as pd
from urllib.request import urlretrieve, urlopen
from datetime import datetime
import math
import re
import numpy as np
from bs4 import BeautifulSoup

data_destination_path = "C:\\wamp64\\www\\projet_big_data_team2\\Docs collecte"

# download the file csv
presidential_state_toplines_source_url = 'https://query.data.world/s/6hgyx2ofu4o2qef6fng5ljb5f3t45n'
presidential_state_toplines_csv_destination_path = os.path.join(data_destination_path, 'presidential_state_toplines_2020.csv')

# download the file from internet
urlretrieve(presidential_state_toplines_source_url,presidential_state_toplines_csv_destination_path )


# Display the file informations
info = os.stat(presidential_state_toplines_csv_destination_path)
print(info)
print("size (Mo): ", round(info.st_size/1000000, 3))
print("last_update: ", datetime.fromtimestamp(info.st_ctime))

# Explore the file
df = pd.read_csv(presidential_state_toplines_csv_destination_path, sep=";", nrows=1000)
df.info()