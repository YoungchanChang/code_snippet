도커 네트워크


# 도커 네트워크 추가한 채로 실행하기
docker run -it -p 5300:5300 --network test_net --name test image:v1 /bin/bash

# 네트워크 내부 url
url = "컨테이너 이름:포트/경로"로 활용
url = "http://test_container:5007/test_path"

# container 내부에 들어가기


docker container exec -it elasticsearch bash


/usr/share/elasticsearch 에 존재



### dockerfile로부터 이미지 빌드하기
 docker build -t bokji_qna:v1 .         
가
### 도커 run하기
docker run -it -p 5302:9100 --network=host --name bokji_qna bokji_qna:v1 /bin/bash

docker run -it -d 5302:9100 --network=parlai_net --name bokji_qna bokji_qna:v1

### 도커 exec하기
docker exec -it bokji_qna bash

### rebuild 도커 컴포즈
 To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.

docker-compose -d

docker network connect host bokji_qna


https://somjang.tistory.com/m/308


# 도커 빌드하기
docker build -t sample:v1 .
docker run -it -p 5305:5305 --network=parlai_net --name test sample:v1 bash

도커 파일 복사

### 도커 파일을 로컬로 복사
docker cp tmp_container:/root/data/test.md ~/data/

### 로컬 파일을 도커에 복사
- 이미 실행중인 도커에는 아래와 같이 복사를 해야한다.
docker cp ~/data/test.md tmp_container:/root/data/
