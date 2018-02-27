import spiderFunction
import requests
import re
from lib import FMysql
from bs4 import BeautifulSoup
from download import Download

start_html = 'https://news.tongji.edu.cn/classid-5.html'
base_html = 'https://news.tongji.edu.cn'
download = Download()
mysql = FMysql.FMysql()
Soup = download.get(start_html)
max_page = Soup.find('div', class_='pager').find_all('a')[-1]['href']
start = str(max_page).rfind('-')
end = str(max_page).rfind('.')
max_page = str(max_page)[start + 1:end]

for page_num in range(1, int(max_page)):
    base_page_html = base_html + '/classid-5-'
    page_html = base_page_html + str(page_num) + '.html'
    Soup = download.get(page_html)
    all_a = Soup.find_all('div', class_='news_list')[2].find_all('a', attrs={'title': True})
    for a in all_a:
        a = base_html + '/' + a['href']
        # print(a)
        left = a.rfind('-t')
        right = a.rfind('id')
        id = a[right + 3:left]
        if not mysql.isIdExist('tongji_university_news', id):
            Soup = download.get(a)
            title = Soup.find('h1', class_='news_title').get_text()
            info = Soup.find('div', class_='news_info').get_text()
            time = re.search(r"(\d{1,2}/\d{1,2}/\d{4})", info).group()
            time = time.replace('/', '-')
            time = time[6:] + '-' + time[0:5]
            content = str(Soup.find('div', class_='news_content').get_text())
            row = {'title': title, 'time': time, 'content': content, 'url': a, 'id': id}
            mysql.create(row, 'tongji_university_news')
            # print(title)
            # print(info)
            # print(time)
            # print(content)
# all_a = Soup.find_all('div', class_="news_list")[2].find_all('a', attrs={"title": True})
#
# for a in all_a:
#     if not mysql.isTitleExist('tongji_university', a['title']):
#         title = a['title']
#         url = a['href']
#         dict_url = {'title': title, 'url': url}
#         mysql.create(dict_url, "tongji_university")
