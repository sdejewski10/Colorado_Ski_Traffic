### LIBRARIES ###
import pyppdf.patch_pyppeteer
from bs4 import BeautifulSoup, SoupStrainer
import requests
from requests_html import HTMLSession
import pandas as pd
import time
from time import sleep
import os
from os.path import basename, join
from random import randint
from urllib.request import Request, urlopen

t0 = time.time()  ###<--- Starts timer to see how long code takes to run

###DAILY SUMMARY

# https://www.ncdc.noaa.gov/snow-and-ice/daily-snow/CO/snowfall/20200130

year = ['16', '17', '18', '19'] ##<--- SCRAPING FROM 2016 THROUGH 2019
month = ['01','02','03','04','05','06','07','08', '09','10','11','12']
days_list = ['01','02','03','04','05','06','07','08', '09','10','11','12','13','14','15','16', '17', '18', '19',
'20','21','22','23','24','25','26','27','28','29','30','31']

url_list = []

years_urls = []
def url_building():     
    for y in year:
        base_url = 'https://www.ncdc.noaa.gov/snow-and-ice/daily-snow/CO/snowfall/20{}'.format(y)
        years_urls.append(base_url)
    
    for y in years_urls:
        for m in month:
            for d in days_list:
                inter_url = y+(m)+(d)
                url_list.append(inter_url)

url_building()
print(url_list[:3])

selectors_list = []
for i in range(1,31):
    selectors = 'daily-data > tbody > tr:nth-child(327) > td.day.d{}'.format(i)
    selectors_list.append(selectors)


def scraping():
    for u in url_list:
        print(u)
        req = Request(u, headers={'User-Agent':'Mozilla/5.0'})
        webpage = urlopen(req).read()
        soup = BeautifulSoup(webpage, features = 'lxml')
        for s in selectors_list:
            print(s)
            snow_data = soup.select(s)
            print(snow_data)
            sleep(5)

scraping()
    
#daily-data > tbody > tr:nth-child(1) > td.day.d1.selected

#daily-data > tbody > tr:nth-child(327) > td.day.d1

//*[@id="daily-data"]/tbody/tr[327]/td[8]

//*[@id="daily-data"]/tbody/tr[327]/td[9]