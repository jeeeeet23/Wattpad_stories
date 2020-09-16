# importing the libraries
from bs4 import BeautifulSoup
import logging
import requests
import re
import json
# import pprint

logging.basicConfig(level=0)


def remove_html_tags(text):
    """Remove html tags from a string"""
    clean = re.compile('<.*?>')
    return re.sub(clean, '', text)


def Chapterdata(ChapterUrl):
    headers = {'user-agent': 'Mozilla/5.0'}
    res = requests.get(ChapterUrl, headers=headers).text
    soup = BeautifulSoup(res, 'lxml')
    output = []
    for all_paras in soup.find_all('p', {'data-p-id': re.compile('.*')}):
        all_paras_no_html = remove_html_tags(str(all_paras))
        output.append(all_paras_no_html)
    output = ''.join(output)
    return output


def ChapterNum(ChapterUrl):
    # ChapterUrl = 'https://www.wattpad.com/amp/617837280'
    headers = {'user-agent': 'Mozilla/5.0'}
    res = requests.get(ChapterUrl, headers=headers).text
    soup = BeautifulSoup(res, 'lxml')
    links_with_text = []
    numbersRegex = re.compile(r'\d\d\d\d\d\d\d\d\d')
    # attrs={'class': re.compile(r"^product$")}
    for link in soup.find_all('a', attrs={'part-navigate'}):
        chpNum = numbersRegex.search(str(link))
        links_with_text.append(chpNum.group())
    return links_with_text


def CompleteUrls(ChapterUrl):
    multiUrls = []
    url = 'https://www.wattpad.com/amp/'
    for i in ChapterNum(ChapterUrl):
        newUrl = url + i
        multiUrls.append(newUrl)
    return multiUrls


def CompleteChaps():
    all_links = CompleteUrls('https://www.wattpad.com/amp/617837280')
    AllChaps = {}
    for i in range(len(all_links[:2])):
        chaps = Chapterdata(all_links[i])
        AllChaps['Chapter_{}'.format(i+1)] = chaps
    return(AllChaps)


story = CompleteChaps()

with open('Story_small.json', 'w') as outfile:
    json.dump(story, outfile)

# pprint.pprint(CompleteUrls('https://www.wattpad.com/amp/617837280'))
# logging.debug(Chapterdata('https://www.wattpad.com/amp/617837280'))
# logging.debug(ChapterNum('https://www.wattpad.com/amp/617837280'))
# logging.debug(CompleteUrls('https://www.wattpad.com/amp/617837280'))
# logging.debug(CompleteChaps())
