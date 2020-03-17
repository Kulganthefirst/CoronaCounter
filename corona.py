#!/usr/bin/python

import requests
from bs4 import BeautifulSoup
import time

country = "Belgium"
URL = 'https://www.worldometers.info/coronavirus/'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')
search = soup.select("div tbody tr td")

start = -1

for i in range(len(search)):
    if search[i].get_text().find(country) !=-1:
        start = i
        break

data = []

for i in range(1,8):
    try:
        data += [search[start+i].get_text()]
    except:
        data += [0]

#message = "Total infected = {}, New Case = {}, Total Deaths = {}, New Deaths = {}, Recovred = {}, Active Case = {}, Serious Critical = {}".format(*data)
message = "Total infected = {}\nNew Case = {}\nTotal Deaths = {}\nNew Deaths = {}\nRecovred = {}\nActive Case = {}\nSerious Critical = {}".format(*data)

print message;
