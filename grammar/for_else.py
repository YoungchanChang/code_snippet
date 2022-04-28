"""
목표 0부터 10까지 있는 숫자 중에 `11` 데이터가 없을 때 처리.
"""


def before_for_else():
    """for else구문 사용 전 코드"""
    flag = True
    found_data = 11
    for i in range(0, 10, 1):
        if i == found_data:
            flag = False
            break
    if flag:
        print("data not found")


def after_fore_else():
    """for else구문 사용 후 코드"""
    found_data = 11
    for i in range(0, 10, 1):
        if i == found_data:
            break
    else:
        print("data not found")


if __name__ == "__main__":
    before_for_else()
    after_fore_else()