import requests
from bs4 import BeautifulSoup
import time
# URL

url = 'https://dota2.fandom.com/wiki/Table_of_hero_attributes'

page = requests.get(url)

soup = BeautifulSoup(page.content, "html.parser")



table = soup.find('tbody')
#print(table)
#print(table)

headers = []

for i in table.find_all('th'):
    title=i.text
    headers.append(title)
    
#print(headers)

all_tr_data = table.find_all('tr')

hero_attr_data = []
for row in all_tr_data:
    row_data = row.find_all('td')
    row = [i.text for i in row_data] 
    hero_attr_data.append(row)
    print(row)

print(hero_attr_data)

import pandas as pd

data = pd.DataFrame(hero_attr_data)

data.to_csv('Dota_2_Hero_attributes_data.csv')






