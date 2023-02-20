import mal_scraper

user_anime_list = mal_scraper.get_user_anime_list('Tedro7')

data = user_anime_list

import pandas as pd

df = pd.DataFrame(data)

df.to_json('MAL_user_list.json')