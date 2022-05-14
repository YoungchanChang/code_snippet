"""
리스트 컴프리헨션
리스트를 만들 때 사용. ex) 빈 배열, range() 등
copy()대신 속도를 높일 때 사용
"""
import copy


def list_comp():
    lst = [0] * 10
    for i in range(1, 10):
        lst[i] = i * 2

    lst = [i * 2 for i in range(1, 10)]
    # [2, 4, 6, 8, 10, 12, 14, 16, 18]

    lst = [i for i in range(1, 10)]
    odd = [i for i in range(1, 10) if i % 2 == 0]  # 홀수만 들어간다.
    square = [i ** 2 for i in lst]  # 기존 리스트를 이용하여 제곱수가 들어간 리스트를 만들었다.

def dict_comp():
    names = ['키보드', '마우스', '모니터']
    prices = [150000, 90000, 450000]
    products = {key: value for key, value in zip(names, prices)}
    # {'키보드': 150000, '마우스': 90000, '모니터': 450000}


def set_comp():
    lst = [1, 3, 5, 7, 9, 3, 5, 2, 6, 4, 1, 8, 2]
    uniq = {i for i in lst}  # 중복이 제거된다.
    # set([1, 2, 3, 4, 5, 6, 7, 8, 9])


if __name__ == "__main__":
    import time

    deep_copy = []
    st = time.time()
    for i in range(0, 10000, 1):
        deep_copy = copy.copy([i * 2 for i in range(1, i)])
    et = time.time()
    print("copy 걸린 시간 : ", et-st) # 3.628

    list_copy = []
    st = time.time()
    for i in range(0, 10000, 1):
        list_copy = [x for x in [i * 2 for i in range(1, i)]]
    et = time.time()
    print("list 끝난 시간 : ", et - st) # 4.291

