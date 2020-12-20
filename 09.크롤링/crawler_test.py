'''
1. 원하는 웹페이지에 접속하여 HTML 데이터를 받아온다
2. 받아온 HTML 데이터를 분석가능한 형태로 가공한다.
3. 원하는 데이터를 추출한다.
'''

import requests
from bs4 import BeautifulSoup
from requests_html import HTMLSession

response = requests.get('https://www.naver.com')
bs = BeautifulSoup(response.text, 'html.parser')



# session = HTMLSession()
# response = session.get('https://www.naver.com')
# print(response.html.links)

# print(response.status_code)
# print(response.headers)
# print(response.text)