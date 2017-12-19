import requests
from bs4 import BeautifulSoup
import re

def  getHeaders():
    return {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'
}

def getHtml(url,headers):
    return requests.get(url,headers=headers)

def getSoup(html,xml):
    return BeautifulSoup(html.text,xml)

