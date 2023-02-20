import requests
from bs4 import BeautifulSoup
import time
# URL

url = 'https://dota2.fandom.com/wiki/Dota_2_Wiki'

page = requests.get(url)

soup = BeautifulSoup(page.content, "html.parser")

#all_a = soup.findAll("")

#for hero in all_a:
    #print(hero.get('title'))
    
all_div = soup.find_all("div", {"class":"heroentrytext"})

hero_names = []
for name in all_div:
    hero_names.append(name)
    
print(hero_names)

import pandas as pd

hero_df = pd.DataFrame(hero_names)

hero_df.to_csv('hero_name.csv')