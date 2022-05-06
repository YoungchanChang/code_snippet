"""
get_even_data()
빵과 음료수같이 짝이 있는 문제에 사용.
음료수를 받았는데 빵을 못 받은 경우를 구할 때 사가
"""


def get_even_data(s):
    c = 0
    for x in s:
        if x == '빵':
            c += 1
        else:
            c -= 1
        if c < 0:
            return False
    return c == 0