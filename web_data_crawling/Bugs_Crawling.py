# 파일명 : Bugs_Crawling.py

from bs4 import BeautifulSoup
import warnings
import requests
import csv
from time import sleep
from shutil import rmtree
from os.path import isdir
from os import mkdir

warnings.filterwarnings(action = 'ignore')

def bugs_songinfo(tr):
    rank = int(tr.find('strong').text)
    try:
        title = tr.find('p', {'class':'title'}).find('a').text
    except:
        title = tr.find('p', {'class':'title'}).find('span', '') .text
        
    artist = tr.find('p', {'class':'artist'}).find('a').text 
    album = tr.find('a', {'class':'album'}).text
    img_url = tr.find('img').get('src').split('?')[0]
    row = [rank, title, artist, album, img_url]
    return row

def write_csv(filename, rows):
    file = open(filename, 'w', newline = '', encoding = 'utf-8-sig')
    csvfile = csv.writer(file)
    csvfile.writerows(rows)
    file.close()

def write_jpeg(img_url, filename):
    response = requests.get(img_url)
    content = response.content
    file = open(filename, 'wb')
    file.write(content)
    file.close()
    
# ----------------------------
### test ###
date = "20210401"
url = f"https://music.bugs.co.kr/chart/track/day/total?chartdate={date}"

response = requests.get(url)
text = response.text
html = BeautifulSoup(text, 'html.parser')
tr_list = html.select('table.list > tbody > tr')
tr17 = tr_list[17]
tr18 = tr_list[18]

print(tr17.find('strong').text)
print(tr18.find('strong').text)

print(tr17.find('p', {'class':'title'}).find('a').text)
print(tr18.find('p', {'class':'title'}))

#tr18.find('p', {'class':'title'}).find_all('span')[1].text
tr18.find('p', {'class':'title'}).find('span', '')


# ----------------------------
year = 2023
month = 1

for month in range(1,13):
    day = 1
    date = f"{year}{month:0>2}{day:0>2}"
    url = f"https://music.bugs.co.kr/chart/track/day/total?chartdate={date}"

    path = f"csv/bugs_{year}.{month:0>2}.{day:0>2}"
    if isdir(path): rmtree(path)
    mkdir(path)
        
    response = requests.get(url)
    text = response.text
    html = BeautifulSoup(text, 'html.parser')
    tr_list = html.select('table.list > tbody > tr')
    rows = []
    for tr in tr_list:
        *row, img_url = bugs_songinfo(tr)
        rank = row[0]

        img_filename = f'{path}/{rank}.jpeg'
        write_jpeg(img_url, img_filename)
        
        rows.append(row)
    filename = f'{path}/bugs_chart.csv'
    write_csv(filename, rows)
    sleep(2)

# ----------------------------
### test ###
date = '20210401'
url = f"https://music.bugs.co.kr/chart/track/day/total?chartdate={date}"
response = requests.get(url)
text = response.text
html = BeautifulSoup(text, 'html.parser')
tr_list = html.select('table.list > tbody > tr')


# ----------------------------
### test ### 
tr = tr_list[0]
img_url = tr.find('img').get('src').split('?')[0]
response = requests.get(img_url)
content = response.content
file = open('csv/연습.jpeg', 'wb')
file.write(content)
file.close()