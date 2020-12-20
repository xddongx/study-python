import requests
from bs4 import BeautifulSoup

query = '파이썬강좌'
url = 'https://s.search.naver.com/p/blog/search.naver?where=blog&api_type=1&query={}&start=1'.format(query)
r = requests.get('url')
bs = BeautifulSoup(r.text, 'lxml')



