# 파일명 : Melon_Crawling.py

from bs4 import BeautifulSoup
import warnings
import requests
import csv
from time import sleep
from shutil import rmtree
from os.path import isdir
from os import mkdir

warnings.filterwarnings(action = 'ignore')

def melon_songinfo(tr):
    pass


def write_csv(filename, rows):
    pass
    
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) Edg/126.0.0.0'}

url = "https://www.melon.com/chart/index.htm"
response = requests.get(url, headers = headers)
#response.headers['Content-Type']
text = response.text
# text를 file = open ...하여 실제 원하는 페이지가 맞는지 확인하는 작업을 하는 것을 권장

html = BeautifulSoup(text, 'html.parser')

# 멜론 실시간 순위 사이트를 크롤링하여 csv/melon.csv 파일로 저장


tr_list = html.select('table > tbody > tr')
rows = []
for tr in tr_list:
    rank = tr.find('span', {'class' : 'rank'}).text
    title = tr.find('div', {'class':'ellipsis rank01'}).find('a').text
    artist = tr.find('div', {'class':'ellipsis rank02'}).find('a').text
    album = album = tr.find('div', {'class':'ellipsis rank03'}).find('a').text
    row = [rank, title, artist, album]
    rows.append(row)

file = open('csv/melon_chart.csv', 'w', newline = '')
csvfile = csv.writer(file)
csvfile.writerows(rows)
file.close()