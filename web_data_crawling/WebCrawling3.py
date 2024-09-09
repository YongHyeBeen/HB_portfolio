# 파일명 : WebCrawling3.py

from bs4 import BeautifulSoup
import warnings

warnings.filterwarnings(action = 'ignore')

file = open('html/table.html', 'r', encoding = 'utf-8')
read =file.read()
file.close()
print(type(read))
print(read[:350])

# HTML 파일 생성(notepad) => kitri 기준 경로 C:\Users\kitri\Desktop\Source\html
"""
<class 'str'>
<html>
    <head>
	<title> </title>
	<style>
	    table {border:1px solid #000000;}
	    table td {border:1px solid #ff0000; color:red; width:50px; text-align:center;} 
	    table th {border:1px solid #0000ff; color:blue;}
	</style>
    </head>
    <body>
	다음의 테이블의 예입니다.<br>
	<table>
	    <thead>
	        <tr>
		<th>id</th>
		<th>name</th>
		<th>ag
"""

html = BeautifulSoup(read, 'html.parser')
# print(type(html))

#html.find('td')
#html.find_all('tr')
# 태그의 개수를 확인하기 위해서는 find_all로 확인 후 len 함수로 찾아야 함(2개 이상일 때)
# html.find_all('table')[0].find('23')
# fine_all은 해당 태그의 개수를 확인하기 위해 사용하는 것

# html.find('table').find('23')
# html.find_all('table')[0]

## len(html.find('table').find('tbody').find_all('tr'))    ==> 4개의 행 찾기
# tag1 -> tag2 -> tag3으로 된 블럭들을 리스트화
# => xxx.find('tag1').find('tag2').fine_all('tag3')
# ** find_all()은 리스트로 반환받기 때문에 find_all을 사용할 때는 인덱스를 사용하여야 하고, 마지막에만 사용하는 것이 좋음
# 마지막 태그전의 tag들은 find() 메소드를 이용하고, 최종 tag에만 find_all() 메소드를 이용하여 검색해야 함
# tr_list = (html.select('table > tbody > tr'))
#tr_list = html.find('table').find('tbody').find_all('tr')

tr_list = html.find('table').find('tbody').find_all('tr')

rows = []
for tr in tr_list:
    td_list = tr.find_all('td')
    row = []
    for td in td_list:
        data = td.text
        row.append(data)                         # row.append(td.text)
    rows.append(row)
rows

import requests

url = "http://192.168.0.131"
response = requests.get(url)    # r, resp

print("헤더 전체 : ",response.headers, end = "\n\n")
print("컨텐츠 종류 : ",response.headers['Content-Type'])   
print("컨텐츠 용량 : ", response.headers['Content-Length'])

text = response.text
html = BeautifulSoup(text, 'html.parser')


ul_list = html.find_all('ul')

rows = []
for ul in ul_list:
    li_list = ul.find_all('li')
    row = []
    for li in li_list:
        row.append(li.text)
    rows.append(row)

rows

url = "http://192.168.0.101"
response = requests.get(url)

#print("헤더 전체 : ", response.headers, end = "\n\n")
#print("컨텐츠 종류 : ", response.headers['Content-Type'])

text = response.text
html = BeautifulSoup(text, 'html.parser')

tr_list = html.find('table').find('tbody').find_all('tr')

rows = []
for tr in tr_list:
    no = tr.find('td', {'class':'number'}).text
    name = tr.find('td', {'class':'professor'}).text
    lec= tr.find('td', {'class':'lecture'}).text
    grade = tr.find('td',{'class':'grade'}).text
    eva = tr.find('td', {'class':'evaluation'}).text
    row = [no, name, lec, grade, evaluation]
    rows.append(row)
    
rows
#print(tr.find('td'))              # >>> tr = tr_list[0] / >>> tr.find('td')로 확인하면 편리함

# 테스트 코드(for문에 들어갈 내용들을 찾는 테스트)
tr = tr_list[0]
#print((tr.find_all('td')[1]))
#print((tr.find_all('td')[2]))
#print(tr.find('td', {'class':'professor'}))
#print(tr.find('td', {'class':'lecture'}))

no = tr.find('td', {'class':'number'}).text
name = tr.find('td', {'class':'professor'}).text
lec= tr.find('td', {'class':'lecture'}).text

row = [no, name, lec]
print(row)

import csv
file = open('csv/professors.csv', 'w', newline ='')
csvfile = csv.writer(file)
#csvfile.writerow()   
csvfile.writerows(rows)
file.close()