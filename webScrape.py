import requests
import re
from bs4 import BeautifulSoup
import pandas as pd
import lxml
import math
import random

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'}


def getNouns():
    # Get data from website
    r = requests.get("https://eslgrammar.org/list-of-nouns/", headers=headers)
    html = r.text
    # Read HTML using beautiful soup
    soup = BeautifulSoup(html, 'html.parser')

    dfList = pd.read_html(r.text)  # Parses all tables into a list
    nouns = dfList[0]  # Get first table from lists
    nouns.head()
    nouns = nouns.fillna("Monster")
    return nouns


def getVerbs():
    # Get verbs list
    r = requests.get("https://7esl.com/english-verbs/", headers=headers)

    html = r.text

    soup = BeautifulSoup(html, 'html.parser')

    results = soup.find_all(['li', 'strong'], {'class': None})

    verbs = []
    for result in results:
        if len(result.text) <= 12 and "." not in result.text and " " not in result.text:
            splitWord = result.text.replace("\xa0", ' ').split("\u2013", 1)
            subString = splitWord[0]
            verbs.append(subString)

    return verbs


def getGenres():
    # Get verbs list
    r = requests.get("https://reference.yourdictionary.com/books-literature/different-types-of-books.html",
                     headers=headers)

    dfList = pd.read_html(r.text)  # Parses all tables into a list
    df = dfList[0]  # Get first table from lists
    df.head()
    print(df[0][28])
    return df


def getWordCount():
    return math.ceil(random.randint(600, 1200) / 100) * 100


def getPOV():
    r = requests.get("https://thewritepractice.com/point-of-view-guide/")
    html = r.text
    soup = BeautifulSoup(html, 'html.parser')
    strong_el = soup.find_all('strong')
    pov = []
    for i in range(0, 4):
        pov.append(strong_el[i].text)
    return pov


def getTheme():
    r = requests.get('https://literarydevices.net/a-huge-list-of-common-themes/')
    html = r.text
    soup = BeautifulSoup(html, 'html.parser')
    results = soup.find_all(['li', 'br'], {'class': None})

    themes = []
    for result in results:
        if len(result.text) <= 12 and "." not in result.text:
            splitWord = result.text.replace("\xa0", ' ').split("\u2013", 1)
            subString = splitWord[0]
            themes.append(subString)

    return themes


def getTimePeriod():
    return math.ceil(random.randint(1900, 2022) / 10) * 10

getNouns()