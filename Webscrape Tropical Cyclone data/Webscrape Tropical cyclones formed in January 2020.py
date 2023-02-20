import requests
from bs4 import BeautifulSoup

url = 'https://en.wikipedia.org/wiki/Tropical_cyclones_in_2020'

page = requests.get(url)

soup = BeautifulSoup(page.content, "html.parser")

# Gathering data from the table.

table_data = soup.find('table', class_="wikitable sortable")
#(table_data)

headers = []

# Scraping headers from the table
for h in table_data.find_all('th'):
    headers.append(h.text.strip())


data_rows = table_data.find_all('tr')

rows_data = []
for row in data_rows:
    value = row.find_all('td')
    cleaned_value = [ele.text.strip() for ele in value]
    rows_data.append(cleaned_value)

print(rows_data)

import pandas as pd

dataset = pd.DataFrame(rows_data, columns=headers)

dataset.to_csv('Tropical cyclones formed in January 2020.csv')

