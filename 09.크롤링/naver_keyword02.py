import requests
from bs4 import BeautifulSoup
from selenium import webdriver

# driver = webdriver.Chrome('C:/chromedriver.exe')

# driver.implicitly_wait(3)

# driver.get('https://www.naver.com')

# html = driver.page_source
response = requests.get('https://www.naver.com')
soup = BeautifulSoup(response.text, 'html.parser')

menu_list = []

ul_list = soup.select('#NM_FAVORITE > div.group_nav > ul.list_nav.type_fix > li > a')


for li in ul_list:
    menu_list.append(li.text)

# 덜 들어온다....
new_ul = soup.select('#NM_FAVORITE > div.group_nav > ul.list_nav.NM_FAVORITE_LIST > li > a')

for li in new_ul:
    menu_list.append(li.text)

print(menu_list)


