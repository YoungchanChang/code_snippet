"""데이터 정보 담는 자료형
# ref : https://docs.python.org/ko/3/library/dataclasses.html
"""
from collections import namedtuple
from typing import Optional, List
from dataclasses import dataclass, field


def set_named_tuple():
    # 튜플 선언
    Pointer = namedtuple('Pointer', ['x', 'y']) # immutable 객체.
    test_tuple = namedtuple("test_tuple", "col1, col2, col3")
    item1 = test_tuple("python", "deep_learning", "3")

    p = Pointer(11, y=22)
    print(p.x, p.y)

    d = {'x' : 100, 'y': 200 }
    p = Pointer(**d) # 딕셔너리 형태로 값을 삽입
    print(p.x)

    print(p._asdict()) # 딕셔너리 형태로 출력

    print(p._fields) # 변수 이름 출력

    re_p = p._replace(x = 1000) # 값 변경
    print(re_p)

    print(p.index(200)) # value의 인덱스 출력. 가장 처음 값 출력.

    print(p.count(100)) # 개수를 센다. 앞의 값이 아닌 value를 출력.


@dataclass
class MecabWordCategory:
    category: int
    start_idx: Optional[int] = None
    end_idx: Optional[int] = None
    entity: Optional[str] = None
