# 파일명 : NaverStock_Crawling

from bs4 import BeautifulSoup
import re
import warnings
import requests
import csv
from time import sleep
from shutil import rmtree
from os.path import isdir
from os import mkdir

warnings.filterwarnings(action = 'ignore')

# 하루치 데이터를 추출해내는 함수 정의
def extract_1day(tr):
    td_list = tr.find_all('td')
    # 필요없는 상승 하락 같은 문자가 들어있는 요소 제거
    del td_list[2]
    row = []
    
    # 날짜를 뽑아, '-'로 변경
    date = td_list.pop(0).find('span').text.replace('.', '-')
    row.append(date)
    
    # 나머지 td에 있는 상한가, 하한가 등의 쉼표를 제거하고 정수형으로 변경
    for td in td_list:
        data = int(td.find('span').text.replace(',', ''))
        row.append(data)
    return row
    
# text
#headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) Edg/126.0.0.0'}
#code = "005930"
#page = 1
#url = f"https://finance.naver.com/item/sise_day.naver?code={code}&page={page}"

#response = requests.get(url, headers = headers)
#text = response.text

# 아래의 file = open...은 크롤링하고 싶은 페이지가 정상적으로 확인되는지 html로 확인하는 코드
# (확인되면 해당 코드는 필요 없음)
"""content = response.content
file = open('naver_stock.html', 'w')
read = file.write(text)
file.close()"""

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) Edg/126.0.0.0'}
code = "005930"
# page = 1

rows = []
for page in range(1,51):
    url = f"https://finance.naver.com/item/sise_day.naver?code={code}&page={page}"
    response = requests.get(url, headers = headers)
    text = response.text
    html = BeautifulSoup(text, 'html.parser')
    
    tr_list = html.find('table', {'class':'type2'}).find_all('tr', {'onmouseover' : 'mouseOver(this)'})

    for tr in tr_list:
        row = extract_1day(tr)
        rows.append(row)
    sleep(1)

file = open('csv/naver_Stock.csv', 'w', newline = '')
csvfile = csv.writer(file)
csvfile.writerows(rows)
file.close()

tr = tr_list[0]
td_list = tr.find_all('td')
# 필요없는 상승 하락 같은 문자가 들어있는 요소 제거
del td_list[2]
row = []

# 날짜를 뽑아, '-'로 변경
date = td_list.pop(0).find('span').text.replace('.', '-')
row.append(date)

# 나머지 td에 있는 상한가, 하한가 등의 쉼표를 제거하고 정수형으로 변경
for td in td_list:
    data = int(td.find('span').text.replace(',', ''))
    row.append(data)
    
url = f"https://finance.naver.com/item/sise_day.naver?code={code}&page={page}"
response = requests.get(url, headers = headers)
text = response.text
html = BeautifulSoup(text, 'html.parser')

tr_list = html.find('table', {'class':'type2'}).find_all('tr', {'onmouseover' : 'mouseOver(this)'})
rows = []
row = []
for tr in tr_list:
    row = extract_1day(tr)
    rows.append(row)
rows