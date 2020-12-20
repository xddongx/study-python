import requests
from bs4 import BeautifulSoup

def get_movie_point(start, end=1):
    results = []
    for i in range(start, end+1):
        url = 'https://movie.naver.com/movie/point/af/list.nhn?&page={}'.format(i)
        r = requests.get(url)
        bs = BeautifulSoup(r.text,'lxml')

        trs = bs.select('table.list_netizen > tbody > tr')

        for tr in trs:
            number = tr.select_one('td.ac.num').text
            writer = tr.select_one('td.num > a.author').text
            tr_data = tr.select_one('td.title')
            title = tr_data.select_one('a').text
            point = tr_data.select_one('div > em').text

            [x.extract() for x in tr_data.select('a')]
            [x.extract() for x in tr_data.select('div')]
            [x.extract() for x in tr_data.select('br')]

            contents = tr_data.text.strip()
            results.append({
                'number': number,
                'movie': title,
                'writer': writer,
                'point': point,
                'contents': contents,
            })
    return results
movies = get_movie_point(1,1)
print(movies)