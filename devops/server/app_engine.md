# 앱엔진에 배포하기

gcr.io/<dir>/appengine:<app-name>-v1 
docker run -it <app-name>:v1 /bin/bash
1. 마지막 컨테이너에서 git 땡겨오기

2. 이미지 만들기
docker commit eager_lalande(컨테이너이름) <app-name>:v1(만들이미지이름
)

3. 이미지로 빌드 -> 도커파일있는 폴더로 이동

4. 이미지 빌드
docker build —tag gcr.io/<dir>/<app-name>:v1 ./

5. 빌드된 이미지 잘 작동하는지 확인하기
docker run -d -p 5001:5001 gcr.io/<dir>/<app-name>:v1
 
6. 포스트맨으로 확인 후 구글 도커 레지스트리에 올리기
gcloud docker — push gcr.io/<dir>/<app-name>:v1

7. gcp 가서 배포하기

# 도커 구글에 쓰기
- 도커에 구글 이미지 커밋하기
$ docker commit elastic_mrc gcr.io/<dir>/elastic_mrc:v1

- 이미지 푸시하기
$ docker push gcr.io/<dir>/<app-name>:v1

- 특정 도커에서 풀하기
$ docker pull gcr.io/<dir>/<app-name>:v1

# Tip
- 포인트는 <dir>이 저장소로 쓰인다는 점
- 이름을 제대로 설정해야한다.
