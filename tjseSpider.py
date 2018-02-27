import spiderFunction
import requests
import re
from lib import FMysql
from bs4 import BeautifulSoup
from download import Download

download = Download()

mysql = FMysql.FMysql()

for page_num in range(1, 11):
    start_html = 'http://sse.tongji.edu.cn/Data/List/xwdt'
    start_html += '?page='
    start_html += str(page_num)
    Soup = download.get(start_html)
    all_a = Soup.find('div', class_='right-nr').find('ul').find_all('a')

    for a in all_a:

        article_href = a['href'][a['href'].rfind('/') + 1:]
        if not mysql.isUrlExist("software_engineering", article_href):
            page_url = "http://sse.tongji.edu.cn/" + a['href']
            page_soup = download.get(page_url)
            article = page_soup.find('div', class_='right-nr')
            article_title = article.find('div', class_='view-title').find('h1').get_text()
            article_time = article.find('div', class_='view-info').find('span').get_text()
            article_time = re.search(r"(\d{4}-\d{1,2}-\d{1,2})", article_time).group()
            article_content = article.find('div', class_='view-cnt').get_text()
            dict_article = {'title': article_title, 'content': article_content, 'time': article_time,
                            'id': article_href}
            mysql.create(dict_article, "software_engineering")
