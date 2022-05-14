

def rotate(key):
    # *key는 껍질(Unpacking)을 벗겨내는 역할을 합니다. [] () {}
    # [[0, 0, 0], [1, 0, 0], [0, 1, 1]] key
    # [0, 0, 0], [1, 0, 0], [0, 1, 1] *key
    # (0, 1, 0), (0, 0, 1), (0, 0, 1) zip(*key)
    # (0, 1, 0), (1, 0, 0), (1, 0, 0) reversed
    # [0, 1, 0], [1, 0, 0], [1, 0, 0] list
    # [[0, 1, 0], [1, 0, 0], [1, 0, 0]] []

    return [list(reversed(i)) for i in zip(*key)]


def create_empty_sec_array():
    """빈 2차원 배열 생성"""
    lst = [[0] * 5 for __ in range(5)]
    print(lst) # [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]


def check_sec_array():
    """2차원 리스트 행과 열로 읽기"""
    row = 3
    column = 4

    for each_row in range(0, row, 1): # step이 1이면 생략 가능
        for each_column in range(0, column, 1):
            print(each_row, each_column)


if __name__ == "__main__":

    ...