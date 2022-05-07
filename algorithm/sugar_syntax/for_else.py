"""
코드 3줄 줄이는 코드
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


def after_for_else():
    """for else구문 사용 후 코드"""
    found_data = 11
    for i in range(0, 10, 1):
        if i == found_data:
            break
    else:
        print("data not found")


if __name__ == "__main__":
    before_for_else()
    after_for_else()