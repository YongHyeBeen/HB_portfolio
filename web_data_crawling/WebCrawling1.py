# 파일명 : WebCrawling1.py

import re
import warnings
warnings.filterwarnings(action = 'ignore')


# HTML 파일 생성(notepad) => kitri 기준 경로 C:\Users\kitri\Desktop\Source\html
"""
<html>
    <head>
	<title> 용혜빈의 홈페이지  </title>
	<style>

	</style>
    </head>
    <body>
	안녕하세요.<br>
	용혜빈의 홈페이지에 오신 것을 환영합니다.<br>
	<ul>내가 좋아하는 것들
	    <li>게임</li>
	    <li>영화</li>
	    <li>음악</li>
	</ul>
	<ul>내가 싫어하는 것들
	    <li>청소</li>
	    <li>잔소리</li>
	    <li>그냥</li>
	</ul>
    </body>
</html>
"""

file = open('html/index.html','r', encoding ="utf-8")
read = file.read()
file.close()

print(read)


# like = ['게임', '영화', '음악']

pat = re.compile("<li>(?P<text>.*)</li>")
matchs = pat.finditer(read)
like = []
for match in matchs:
    data = match.group('text')
    like.append(data)

like

""" rows = [
['게임', '영화', '음악']
['청소', '잔소리', '그냥']
]
"""
# 2개의 for문을 이용하여 2차원 리스트로 만들기
pat = re.compile("<ul>.*?</ul>", re.DOTALL)
ul_list = pat.finditer(read)

rows = []
for ul in ul_list:
    row = []
    text = ul.group()
    pat = re.compile("<li>(?P<text>.*)</li>")
    li_list = pat.finditer(text)
    for li in li_list:
        data = li.group('text')
        row.append(data)
    rows.append(row)
rows