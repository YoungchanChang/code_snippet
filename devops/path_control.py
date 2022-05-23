"""
참조 : https://engineer-mole.tistory.com/191

https://wikidocs.net/39
파이썬 경로 조작법엔 2가지가 존재.

Path객체 사용
os내장 모듈 사용
Path객체가 os내장 모듈보다 더 가독성이 좋음.
예시> 본인의 경로 읽는 함수
"""

from pathlib import Path
import os
import sys
BASE_DIR_PATH = Path(__file__).resolve().parent
BASE_DIR_OS = os.path.dirname(os.path.abspath(__file__))

sys.path.append(str(BASE_DIR_PATH))
# 상대 경로 추출
from pathlib import Path
relative_file_path = Path(__file__).resolve().relative_to(Path(__file__).cwd())
# 예시 2> 하위 디렉터리 검색을 쉽게 해주는 함수 비교

# - os를 활용한 로직
import os
for (path, dir, files) in os.walk("c:/"):
    for filename in files:
        ext = os.path.splitext(filename)[-1]
        if ext == '.py':
            print("%s/%s" % (path, filename))


# - Path객체를 활용한 로직
for i in Path.iterdir(BASE_DIR_PATH):
    if i.suffix == ".py":
       print("%s/%s" % (i.parent, i.name))