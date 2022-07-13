# Javascript

- Javascript : HTML을 움직이게 함
- jQuery 
  - Javascript로 HTML을 쉽게 제어
  - HTML의 요소들을 조작하는, 편리한 Javascript를 미리 작성해둔 라이브러리!
- Ajax : 서버에 데이터를 요청하고 받음

# JSON

- JSON : JavaScript Object Notation (JSON)은 Javascript 객체 문법으로 구조화된 데이터를 표현하기 위한 문자 기반의 표준 포맷
- Key:Value 구조. Dictionary 형태의 값임

## 요청방식
- 같은 예금 창구에서도 개인 고객이냐 기업 고객이냐에 따라 가져와야 하는 것 / 처리해주는 것이 다른 것처럼 클라이언트가 요청 할 때에도, "타입"이라는 것이 존재

- GET : 
  - 데이터 조회(Read)를 요청
  - GET 요청은, url뒤에 아래와 같이 붙여서 데이터를 가져옴
  - http://naver.com?param=value&param2=value2 

- POST
  - 데이터 생성(Create), 변경(Update), 삭제(Delete) 요청
  - POST 요청은, data : {} 에 넣어서 데이터를 가져감.
  - data: { param: 'value', param2: 'value2' }

