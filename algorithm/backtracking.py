"""
리스트 값 변환시 사용
특정 조건이 맞지 않으면 반환하지 않을 때 사용
"""


def backtrack_list(input_list: list):
    if input_list == []:
        return "empty"

    if input_list[0] == 1:
        return "do"

    for i in input_list:
        print(i)


if __name__ == "__main__":
    test_list = [0, 1, 2, 3, 4, 5]
    backtrack_list(test_list)