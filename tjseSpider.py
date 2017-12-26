import spiderFunction
import requests
import re
from lib import FMysql
from bs4 import BeautifulSoup

import os

headers = spiderFunction.getHeaders()

start_html = spiderFunction.getHtml('http://sse.tongji.edu.cn/Data/List/xwdt', headers)
Soup = spiderFunction.getSoup(start_html, 'lxml')

all_a = Soup.find('div', class_='right-nr').find('ul').find_all('a')
mysql = FMysql.FMysql()
for a in all_a:

    article_href = a['href'][a['href'].rfind('/') + 1:]
    # article_href=
    if not mysql.isUrlExist("software_engineering", article_href):
        page_url = "http://sse.tongji.edu.cn/" + a['href']
        # print(page_url)
        page_html = requests.get(page_url, headers=headers)
        # print(page_html)
        page_soup = BeautifulSoup(page_html.text, 'lxml')
        article = page_soup.find('div', class_='right-nr')
        article_title = article.find('div', class_='view-title').find('h1').get_text()
        article_time = article.find('div', class_='view-info').find('span').get_text()
        article_time = re.search(r"(\d{4}-\d{1,2}-\d{1,2})", article_time).group()
        article_content = article.find('div', class_='view-cnt').get_text()
        dict_article = {'title': article_title, 'content': article_content, 'time': article_time, 'id': article_href}
        mysql.create(dict_article, "software_engineering")
