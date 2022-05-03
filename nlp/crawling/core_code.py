import requests
from bs4 import BeautifulSoup


def crawl_page():
    res = requests.get('http://v.media.daum.net/v/20170615203441266')
    soup = BeautifulSoup(res.content, 'html.parser')
    mydata = soup.find('title')
    print(mydata.get_text())


def crawl_pages():

    for page_num in range(10):
        if page_num == 0:
            res = requests.get('http://v.media.daum.net/v/20170615203441266')
        else:
            res = requests.get('http://v.media.daum.net/v/20170615203441266' + str(page_num + 1))
        soup = BeautifulSoup(res.content, 'html.parser')

        data = soup.select('h4.card-text')
        for item in data:
            print (item.get_text().strip())