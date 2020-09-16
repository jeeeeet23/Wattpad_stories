# Importing the libraries
import requests
import logging
from bs4 import BeautifulSoup


def getdata(ChpUrl):
    headers = {'user-agent': 'Mozilla/5.0'}
    r = requests.get(ChpUrl, headers=headers).text
    soup = BeautifulSoup(r, 'lxml')
    return r


url = 'https://www.wattpad.com/amp/617837280'
headers = {'user-agent': 'Mozilla/5.0'}
r = requests.get(url, headers=headers)
page = r.text

soup = BeautifulSoup(page, 'lxml')
# element = soup.find_all("a", {"class": "details-navigate"})

logging.warning(page)

# try searching for find_all <p div ...> from paragraph sentence
