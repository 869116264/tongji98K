import spiderFunction
import requests
import re
from bs4 import BeautifulSoup
import os

headers = spiderFunction.getHeaders()

start_html=spiderFunction.getHtml('http://sse.tongji.edu.cn/Data/List/xwdt',headers)
Soup = spiderFunction.getSoup(start_html,'lxml')


all_a = Soup.find('div', class_='right-nr').find('ul').find_all('a')
for a in all_a:
    page_url = "http://sse.tongji.edu.cn/" + a['href']
    # print(page_url)
    page_html = requests.get(page_url, headers=headers)
    # print(page_html)
    page_soup = BeautifulSoup(page_html.text, 'lxml')
    article = page_soup.find('div', class_='right-nr')
    article_title = article.find('div', class_='view-title').find('h1').get_text()
    article_time = article.find('div', class_='view-info').find('span').get_text()
    article_time = re.search(r"(\d{4}-\d{1,2}-\d{1,2})", article_time)
    article_content = article.find('div',class_='view-cnt' ).get_text()
    print(article_title)
    print(article_time.group())
    print(article_content)
