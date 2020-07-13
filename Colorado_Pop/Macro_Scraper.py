### LIBRARIES ###
from bs4 import BeautifulSoup, SoupStrainer
import requests
from requests_html import HTMLSession
import pandas as pd
import time
from time import sleep
import os
from os.path import basename, join
from random import randint

#SETUP#
t0 = time.time()  ###<--- Starts timer to see how long code takes to run
header = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36'}
url = 'https://www.macrotrends.net/states/colorado/population'
print('Setup Successful!')

df_1 = pd.DataFrame()
def population_scrape():
    r = requests.get(url, headers = header)
    df = pd.read_html(r.text)

    population_data = (df[1])
    Colorado_Population = df_1.append(population_data)
    Colorado_Population.to_csv('Colorado_Population.csv', index = False, header = True)

population_scrape()