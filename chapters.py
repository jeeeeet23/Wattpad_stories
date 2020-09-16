# importing the libraries
from bs4 import BeautifulSoup
import requests
import re
import logging


def ChapterNums(ChapterUrl):
    headers = {'user-agent': 'Mozilla/5.0'}
    res = requests.get(ChapterUrl, headers=headers).text
    soup = BeautifulSoup(res, 'lxml')
    adam = []
    for chapNums in soup.find_all('a', {'part-navigate': re.compile(r'\d\d\d\d\d\d\d\d\d')}):
        number = re.findall(chapNums)
        adam.append(number)
    adam = ''.join(adam)
    return(adam)


logging.warning(ChapterNums('https://www.wattpad.com/amp/617837280'))
