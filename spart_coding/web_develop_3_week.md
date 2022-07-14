
# python, 크롤링, mongodb
- python
- 크롤링
- pymongo

## python
- 변수 & 기본연산
- 자료형 : 숫자, 문자형 / 리스트형 / Dictionary형 / 
- 함수
- 조건문
- 반복문 : 리스트의 요소들을 하나씩 꺼내쓰는 형태

## 크롤링

- 데이터를 가져옴

```angular2html
import requests
from bs4 import BeautifulSoup

# 데이터 가져옴
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.naver?sel=pnt&date=20210829',headers=headers)

# 파싱
soup = BeautifulSoup(data.text, 'html.parser')
```

## Database
- 데이터를 쉽게 저장하고, 가져오기 위해서 사용
- DB에는 Index 라는 순서로 데이터들이 정렬
- SQL : 정형화된 데이터베이스. 
- NoSQL : 정형화되지 않은 데이터베이스.