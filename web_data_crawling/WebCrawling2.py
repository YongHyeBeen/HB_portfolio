# 파일명 : WebCrawling2.py

from bs4 import BeautifulSoup
from module import dir2

# HTML 파일 생성(notepad) => kitri 기준 경로 C:\Users\kitri\Desktop\Source\html
"""
'<html>\n
    <head>\n
    \t<title> 용혜빈의 홈페이지  </title>\n
    \t<style>\n\n\t</style>\n
    </head>\n
    <body>\n
    \t안녕하세요.<br>\n
    \t용혜빈의 홈페이지에 오신 것을 환영합니다.<br>\n
    \t<ul>내가 좋아하는 것들\n
    \t<li>게임</li>\n
    \t<li>영화</li>\n
    \t<li>음악</li>\n
    \t</ul>\n
    \t<ul>내가 싫어하는 것들\n
    \t<li>청소</li>\n
    \t<li>잔소리</li>\n
    \t<li>그냥</li>\n
    \t</ul>\n</body>\n
</html>
"""

file = open('html/index.html', 'r', encoding='utf-8')
read = file.read()
file.close()
print(type(read))
read

html = BeautifulSoup(read, 'html.parser')

ul_list = html.find_all('ul')
for ul in ul_list:
    li_list = ul.find_all('li')
    for li in li_list:
        print(li.text)
        print("------------")
    print("===================")
    
    
html = BeautifulSoup(read, 'html.parser')

ul_list = html.find_all('ul')
rows = []
for ul in ul_list:
    li_list = ul.find_all('li')
    row = []
    for li in li_list:
        data = li.text
        row.append(data)
    rows.append(row)
rows