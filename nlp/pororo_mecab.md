카카오 뽀로로를 위한 Mecab 설치

```
카카오 MRC 공식 문서 주소
https://github.com/kakaobrain/pororo
https://kakaobrain.github.io/pororo/
```

Mecab 설치 방법 및 사용자사전 추가 방법

# 공식 가이드 참조하기
기본적으로 https://bitbucket.org/eunjeon/mecab-ko-dic/src/master/ 여기 설명을 따라가면
1.	Mecab-ko 설치 -> mecab-ko-dic 설치 -> python mecab 설치
2.	Mecab-ko 설치
- 다운로드페이지에서 압축파일 /usr/local/lib/에 다운로드

```
wget "https://bitbucket.org/eunjeon/mecab-ko/downloads/mecab-0.996-ko-0.9.2.tar.gz"
wget "https://bitbucket.org/eunjeon/mecab-ko-dic/downloads/mecab-ko-dic-2.1.1-20180720.tar.gz"
```

- tar zxfv mecab-XX-ko-XX.tar.gz (압축풀기 XX는 버전명 혹은 날짜)
- cd mecab-XX-ko-XX
- ./configure
- make
- make check
- sudo su -> 비번 입력
- make install
3.	Mecab-ko-dic 설치
- 다운로드페이지에서 압축파일 /usr/local/lib/에 다운로드
- tar zxfv mecab-ko-dic-XX.tar.gz
- cd mecab-ko-dic-XX
- ./configure
- make
- sudo su -> 비번입력
- make install
4.	Mecab-ko-dic 설치 오류시!!!!
- ./configure 실행 후 make 실행시킬 때 에러가 날 수 있다
- 이럴 때에는 압축푼 폴더를 지운 후 다음의 방법으로 설치하면 됨
- tar xvfz mecab-ko-dic-XX.tar.gz
- cd mecab-ko-dic-XX

automake1.11 설치 후, 위와 동일하게 재시도 혹은,
autogen.sh 실행 후 재시도
$ ./autogen.sh

- autoreconf (추가된부분)
- ./configure
- make
- sudo su -> 비번
- make install

5. Mecab 터미널에서 실행하기
- mecab -d /usr/local/lib/mecab/dic/mecab-ko-dic
- 한글문장입력 -> 결과확인
- ctrl + c (미캡종료)

6.	Mecab python 설치
- pip3 install mecab-python3


+ cp /usr/local/lib/mecab-0.996-ko-0.9.2/mecab-config ~/.pyenv/versions/youtube_api/bin/

+. 미캅 파이썬3 설치
$ pip install python-mecab-ko
https://lovablebaby1015.wordpress.com/2018/09/24/mecab-macos-%EC%84%A4%EC%B9%98-%EC%82%BD%EC%A7%88-%ED%9B%84%EA%B8%B0-%EC%9E%91%EC%84%B1%EC%A4%91/

7.	사용자사전 추가하기
- mecab-ko-dic-XX/user-dic 폴더에 csv 파일을 만든다.
- 읽는방법 열 뒤에 끝부분에 별 5개 (4개아님)
- 사용자 사전 추가시 정해진 명칭 외의 명을 사용하면 사전 추가 안됨 (예 - 지명 O/ 해외지명 X)
- (mecab-ko-dic-XX 폴더 위치에서)
    ./tools/add-userdic.sh
- 위에 add-userdic.sh 파일을 실행 했을 때 오류 발생시
    -> brew install coreutils (coreutils 설치)
- coreutils 설치 후 -> ./tools/add-userdic.sh
- make clean
- sudo su
- make install
8.	사용자 사전 단어 우선 순위 높이기
- 사전을 추가하면 mecab-ko-dic-XX에 user-사용자지정이름.csv 생성됨
- 파일 확인해보면 2-4열에 숫자가 생성 되어 있음
- 2,3열은 인덱스 정보이고 4열이 우선순위임
- 4열의 숫자를 낮춰주면 우선순위 올라감
- make clean
- sudo su
- make install

9.	 테스트서버/운영서버에 사용자사전 추가하기
- 서버에 파일올리기 (ssh 터미널 우측 상단에 톱니바퀴 클릭 후 파일업로드)
- 파일 올라오는 장소는 /home/(user name) -> 무조건 여기로 올라감
- 파일 미캡 딕셔너리 폴더로 이동 (로칼컴퓨터에서 이미 컴파일이 됐었던 사용자사전 파일을 올릴경우)
 mv (사용자사전).csv /usr/local/roja/mecab/mecab-ko-dic-2.0.3-20170922
- 사용자사전 파일 딕셔너리 폴더로 옮긴 후 딕셔너리 폴더로 이동
 cd /usr/local/roja/mecab/mecab-ko-dic-2.0.3-20170922
- 사용자사전 컴파일
 make clean
 sudo su
 make install



### Dictionary에 mecab사전 올리기
- mecab-ko-dic에서 설정해야함

1. 경로이동
cd /Users/youngchan/Desktop/bokji-qa/user_chracter/model/dictionary
2. 사용자 사용 전용 데이터 복사하기
cp user_mecab_dictionary.csv /usr/local/lib/mecab-ko-dic-2.0.1-20150920/user-dic/


3. 이동
cd /usr/local/lib/mecab-ko-dic-2.0.1-20150920/

./tools/add-userdic.sh
make clean
sudo su
make install
	
cd /usr/local/lib/mecab
cp -r dic dic_user_char


mecab -d /usr/local/lib/mecab/dic_user_char/mecab-ko-dic
mecab = MeCab(dicpath="/usr/local/lib/mecab/dic_user_char/mecab-ko-dic")



#############################

# kakao Pororo설치하기
### 경로가 꼬일 수 있으니깐 반드시 새로운 가상환경에 실험해야하고, konlpy는 경로 설정으로 인해 쓰지 말아야 한다.

### mecab설치시 오류 뜰 때
### init 파일 확인하기
from .mecab import MeCabError
from .mecab import MeCab

/usr/local/lib/mecab-ko-dic-2.1.1-20180720/user-dic
user_sentence, entity

# MRC모듈 수행하기

### 뽀로로 설치
$ pip install pororo # 업그레이드 하라는 오류메시지 뜬다.
$ pip3 install --upgrade pip # 업그레이드
$ pip install pororo # 재설치

### mecab 설치
> https://bitbucket.org/eunjeon/mecab-ko-dic/src/master/

- 다운로드페이지에서 압축파일 /usr/local/lib/에 다운로드

### 미캅 한국어 설치
1. 컨피그 파일 복사하기
- 우분투에서 실행하는 명령어 !!! 새로 만들었을 때
cp /usr/local/lib/mecab-0.996-ko-0.9.2/mecab-config ~/.pyenv/versions/{이름}/bin/

cp /usr/local/lib/mecab-0.996-ko-0.9.2/mecab-config ~/.pyenv/versions/wiki_mrc/bin/

/Users/youngchan/Desktop/1thefull/bokji-qa/elastic_search_endpoint/mrc/.python-version

# 순서 지켜야지 pip install mecab이 된다.
2. 미캅 파이썬3 설치
$ pip install python-mecab-ko

3. 미캅 설치
$ pip3 install mecab-python3 로 mecab-python3


# 설치 과정 - 오류 및 설명 포함 별별별별별
TIP : konlpy설치하면 경로 꼬인다. Mecab만 써야 한다.


![스크린샷 2021-03-08 오후 3.36.17.png](:/83195f8714b447518223a322d4001a7e)

뽀로로 포함한 모듈 수행하려면 아래와 같은 에러 발생한다.

```
ModuleNotFoundError: Please install python-mecab-ko with: `pip install python-mecab-ko`
```

! mecab설치 시도
pip install python-mecab-ko

```
No such file or directory: '/Users/youngchan/.pyenv/versions/3.7.9/envs/kakao_mrc/bin/mecab-config': '/Users/youngchan/.pyenv/versions/3.7.9/envs/kakao_mrc/bin/mecab-config'
```
pip install python-mecab-ko

! mecab-config복사하기
cp /usr/local/lib/mecab-0.996-ko-0.9.2/mecab-config /Users/youngchan/.pyenv/versions/3.7.9/envs/kakao_mrc/bin/mecab-config

# 아래와 같은 에러 다시 발생
```
ImportError: dlopen(/Users/youngchan/.pyenv/versions/kakao_mrc/lib/python3.7/site-packages/_mecab.cpython-37m-darwin.so,
```


pip install mecab-python3 로 mecab-python3 설치


###################

# 맥의 특정 경우는 아래 에러가 발생한다.아래 에러 발생
```
AttributeError: module 'mecab' has no attribute 'MeCab'
```

# 경로문제 확인하기

from mecab.mecab import Mecab()을 해야 해결됬다.

__init__ 파일이 달랐다.

# 메캅이 경우에 따라서는 안된다.
Import mecab.mecab으로 해결해야 하는 경우가 있다.
import mecab 우클릭

- __init__.py에 다음 파일 추가

```
from .mecab import MeCabError
from .mecab import MeCab
```

정상 동작

# 다시 처음부터

### 기본설치
find / -name mecabrc ==> 결과 : /usr/local/etc/mecabrc
기본 사전 경로 dicdir =  /usr/local/lib/mecab/dic/mecab-ko-dic로 나옴

확인 1
$ mecab -d /usr/local/lib/mecab/dic/mecab-ko-dic
아헿헿 없었음. 아, 헿헿으로 나옴

확인 2
$ python
import mecab
mecab = mecab.MeCab()
mecab.pos("아헿헿")
인식 안 됨. 아, 헿헿으로 나옴

### 사전 경로 다르게하기

autoreconf

### 사전 경로 추가 후 컴파일
./configure --prefix=/tmp/mecab/dir/dic_user_char --with-dicdir=/usr/local/lib/mecab/dic_user_char/mecab-ko-dic --with-mecab-config=/usr/local/lib/mecab-0.996-ko-0.9.2/mecab-config

### 추가되는 메시지를 잘 읽어보면 나옴. 경로는 여전히 그대로임
-- /usr/local/bin/gmkdir -p '/usr/local/lib/mecab/dic_test'
 /usr/local/bin/ginstall -c -m 644 model.bin matrix.bin char.bin sys.dic unk.dic left-id.def right-id.def rewrite.def pos-id.def dicrc '/usr/local/lib/mecab/dic_test


make clean
make install

확인 1
mecab -d /usr/local/lib/mecab/dic_user_char/mecab-ko-dic

확인 2 - dicpath는 클래스 들어가보면 됨.
import mecab
mecab = mecab.MeCab(dicpath='C:/mecab/mecab-ko-dic')
mecab.pos("아헿헿")

# 본래 사전이 위치한 경로 확인


# mecab 사전 등록의 경로를 설정하고자 할 때
https://bladewalker.tistory.com/655

mecab-0.996이 하는 역할 : 

mecab-ko-dic-0.996이 하는 역할 : 

cp /usr/local/lib/mecab-0.996-ko-0.9.2/mecab-config ~/.pyenv/versions/1thefull/bin/

./configure --prefix=/usr/local/lib/mecab-test



mecab-ko-0.99~는 핵심적인 파일을 함

./configure 후에 make install을 수행할 시 아래 명령어가 뜨면서

### 테스트 수행중

mecabrc 찾아야함
find / -name mecabrc ==> 결과 : /usr/local/etc/mecabrc
내용 dicdir=/usr/local/lib/mecab/dic/mecab-ko-dic

mecab -d /usr/local/lib/mecab/dic_test




autoreconf

./configure --prefix=/tmp/mecab/dir/dic_user_char
--with-dicdir=/usr/local/lib/mecab/dic_user_char/mecab-ko-dic --with-mecab-config=/usr/local/lib/mecab-0.996-ko-0.9.2/mecab-config



###


/usr/local/lib/mecab/dic/mecab-ko-dic 디렉터리에 생김

```
echo To enable dictionary, rewrite /usr/local/etc/mecabrc as \"dicdir = /usr/local/lib/mecab/dic/mecab-ko-dic\"
To enable dictionary, rewrite /usr/local/etc/mecabrc as "dicdir = /usr/local/lib/mecab/dic/mecab-ko-dic"
make[1]: Nothing to be done for `install-exec-am'.
 /usr/local/bin/gmkdir -p '/usr/local/lib/mecab/dic/mecab-ko-dic'
 /usr/local/bin/ginstall -c -m 644 model.bin matrix.bin char.bin sys.dic unk.dic left-id.def right-id.def rewrite.def pos-id.def dicrc '/usr/local/lib/mecab/dic/mecab-ko-dic'
```

사전 2개 다르게 해보자... 그 후에 


컴파일 된 사전은 /usr/local/lib/mecab/dic/mecab-ko-dic 



mecab = Mecab(dicpath='C:/mecab/mecab-ko-dic')



mecab -d /usr/local/lib/mecab/dic/mecab-ko-dic

mecab -d /usr/local/lib/mecab/dic_test/mecab-ko-dic


출처: https://joyhong.tistory.com/129 [옳은 길로..]


참조 >>
https://bladewalker.tistory.com/655

http://openuiz.blogspot.com/2018/12/mecab-ko-mecab-ko-dic.html



mac-os!
https://groups.google.com/g/eunjeon/c/mKcD8OtjwGo



