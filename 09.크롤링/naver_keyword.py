import requests
from bs4 import BeautifulSoup

json = requests.get('https://www.naver.com/srchrank?frm=main').json()
ranks = json.get('data')

for r in ranks:
    rank = r.get('rank')
    keyword = r.get('keyword')
    print(rank, keyword)

'''
select는 list방식
beautifulsoup 사용 select
bs = BeautifulSoup(r.text, 'html.parser')
bs = BeautifulSoup(r.text, 'lxml')          # 좀 더 빠르다.
lists = bs.select('li.realtime_item')

for li in lists:
    title = li.find('sapn', {'class':realtime_item'}).text
    print(title


'''
