"""2차원 배열 문제 나왔을 때 활용할 수 있는 함수들

- 2차원 배열 행, 열 값 하나하나 필요 할 때 : print_second_list()
- 2차원 배열에서 행과 열의 인덱스 값을 조절해야 할 때 : print_enumerate_second_list()
- 배열을 확장시키고 싶을 때 : padding_numpy()
- 빈 2차원 배열을 만들고 싶을 때(numpy): create_second_empty_list_by_np()
- 빈 2차원 배열을 만들고 싶을 때(빈 리스트) : create_second_empty_list_by_list()
- 빈 배열에 특정 값을 삽입하고 싶을 때 : insert_empty_list()

# 상하 좌우 90도 돌리기
- 이차원 배열을 상하 좌우로 돌리고 싶을 때 : roll_second_array()
- 이차원 배열을 90도씩 회전하고 싶을 때 : rotate_second_array()
- 2차원 배열 좌우 상하 뒤집고 싶을 때 : flip_array()
    - 이차원 배열을 역순으로 바꾸고 싶을 때 : reverse_second_array()

# 슬라이싱
- 2차원 배열을 이어 붙이고 싶을 때 : array_concat_array()
- 2차원 배열에서 일부만 자르기 : slicing_second_array()

np.array()
sample[y][x]이다. 첫 괄호 y는 행(높이)을 가리키고, x는 열(길이)를 표시
sample[행-위아래][열-좌우]로 기억

# 리스트로 만들 때 : a.tolist()
ref : https://docs.python.org/release/2.3.5/whatsnew/section-slices.html

"""

import numpy as np


def print_second_list() -> None:
    print("--- BEGIN print_second_list ---")

    test_sec_list = [[1, 2, 3],
                     [4, 5, 6]]

    print("ROW", len(test_sec_list))
    print("COLUMN", len(test_sec_list[0]))

    ROW = 0
    COLUMN = 1

    np_sec_list = np.array(test_sec_list)
    for i in range(0, np_sec_list.shape[ROW], 1): # 기준이 행
        for j in range(0, np_sec_list.shape[COLUMN], 1): # 기준이 열
            print("ROW", i, "COLUMN", j, "VALUES", np_sec_list[i][j])
    print("--- END print_end_second_list ---")


def print_enumerate_second_list() -> None:
    print("--- BEGIN print_enumerate_second_list ---")

    test_sec_list = [[1, 2, 3],
                     [4, 5, 6]]

    print("ROW", len(test_sec_list))
    print("COLUMN", len(test_sec_list[0]))

    ROW = 0
    COLUMN = 1

    np_sec_list = np.array(test_sec_list)
    for row_idx, i in enumerate(range(0, np_sec_list.shape[ROW], 1)): # 기준이 행
        for column_idx, j in enumerate(range(0, np_sec_list.shape[COLUMN], 1)): # 기준이 열
            print("enumerate_ROW", row_idx, "enumerate_COLUMN", column_idx, "enumerate_VALUES", np_sec_list[i][j])
            if row_idx == 2 and column_idx == 1:
                break
    print("--- END print_enumerate_second_list ---")

def padding_numpy() -> np:
    print("--- BEGIN create_padding_numpy ---")

    test_list = [[1, 2], [3, 4]]
    up_padding_size = 4
    up_padding_value = 7
    down_padding_size = 2
    down_padding_value = 8
    left_padding_size = 1
    left_padding_value = 9
    right_padding_size = 3
    right_padding_value = 10
    # 4는 위로, 2는 아래로, 1은 좌로, 3은 아래로
    print("before padding : \n", test_list)
    padding_numpy = np.pad(test_list,
                           ((up_padding_size, down_padding_size), (left_padding_size, right_padding_size)),
                           'constant',
                           constant_values=((up_padding_value, down_padding_value), (left_padding_value, right_padding_value)))
    print("after padding : \n", padding_numpy)
    print("--- END create_end_padding_numpy ---")
    return padding_numpy


def create_second_empty_list_by_np() -> np:
    print("--- BEGIN create_second_empty_list_by_np ---")
    row = 4
    column = 5
    # np.ones()
    zero_numpy = np.zeros((row, column), dtype=int)
    print(zero_numpy)
    print("--- END create_second_empty_list_by_np ---")
    return zero_numpy


def create_second_empty_list_by_list() -> list:
    print("--- BEGIN create_second_empty_list_by_list ---")
    row = 4
    column = 5
    empty_list = [[0] * column for i in range(row)]
    print("row_num :", row, "column_num :", column, "\n", empty_list)
    print("--- END create_second_empty_list_by_list ---")
    return empty_list


def insert_empty_list() -> np:
    ROW = 0
    COLUMN = 1

    print("--- BEGIN insert_empty_list ---")
    # 빈 원소 만들기
    empty_list = create_second_empty_list_by_np()

    # 빈 원소에 넣을 원소 만들기
    insert_value = [[1, 1],
                    [1, 1]]
    insert_value = np.array(insert_value)
    print("empty_list : \n", empty_list)
    print("insert value : \n", insert_value)

    ROW_BEGIN = 2
    ROW_END = ROW_BEGIN + insert_value.shape[ROW] # Not Include
    COLUMN_BEGIN = 1
    COLUMN_END = COLUMN_BEGIN + insert_value.shape[COLUMN]

    empty_list[ROW_BEGIN:ROW_END, COLUMN_BEGIN:COLUMN_END] = insert_value
    print(f"inserted_value : ROW {ROW_BEGIN}, COLUMN {COLUMN_BEGIN}\n",empty_list)

    print("--- END insert_end_empty_list ---")
    return empty_list


def roll_second_array():
    print("--- BEGIN roll_second_array ---")

    ROW = 0
    COLUMN = 1
    ROW_ROLL_DOWN_DISTANCE = 1
    COLUMN_ROLL_RIGHT_DISTANCE = 2

    roll_taget_second_array = [[1,2,3],
                               [4,5,6],
                               [7,8,0]]
    roll_taget = np.array(roll_taget_second_array)
    print("roll_target \n", roll_taget)
    down_roll = np.roll(roll_taget_second_array, ROW_ROLL_DOWN_DISTANCE, axis=ROW) # 행 방향으로 돌리기. 위아래로 돌리기
    print(f"down_roll : ROW {ROW}, DISTANCE : {ROW_ROLL_DOWN_DISTANCE} \n", down_roll)

    right_roll = np.roll(roll_taget_second_array, COLUMN_ROLL_RIGHT_DISTANCE, axis=COLUMN) # 좌우로 돌리기.
    print(f"right_roll : COLUMN {ROW}, DISTANCE : {COLUMN_ROLL_RIGHT_DISTANCE} \n", right_roll)

    column_row_roll = np.roll(roll_taget_second_array, (COLUMN_ROLL_RIGHT_DISTANCE, ROW_ROLL_DOWN_DISTANCE), axis=(COLUMN, ROW)) # 좌우, 위아래로 돌리기
    print(f"column_row_roll : COLUMN {COLUMN} COLUMN_ROLL_RIGHT_DISTANCE : {COLUMN_ROLL_RIGHT_DISTANCE}, ROW {ROW}, ROW_ROLL_DOWN_DISTANCE : {ROW_ROLL_DOWN_DISTANCE} \n", column_row_roll)

    row_column_roll = np.roll(roll_taget_second_array, (ROW_ROLL_DOWN_DISTANCE, COLUMN_ROLL_RIGHT_DISTANCE), axis=(ROW, COLUMN)) # 위아래, 좌우로 돌리기
    print(f"row_column_roll : ROW {ROW} ROW_ROLL_DOWN_DISTANCE : {ROW_ROLL_DOWN_DISTANCE}, COLUMN {COLUMN}, COLUMN_ROLL_RIGHT_DISTANCE : {COLUMN_ROLL_RIGHT_DISTANCE} \n", row_column_roll)


    print("--- END roll_second_array ---")

    return right_roll


def rotate_second_array():
    print("--- BEGIN rotate_second_array ---")
    roll_taget_second_array = [[1,2,3],
                               [4,5,6],
                               [7,8,0]]
    roll_taget = np.array(roll_taget_second_array)

    ANTI_CLOCK_WISE_90 = 1
    ANTI_CLOCK_WISE_180 = 2
    ANTI_CLOCK_WISE_270 = 3
    ANTI_CLOCK_WISE_360 = 4

    print("roll_target \n", roll_taget)
    anti_clock_90 = np.rot90(roll_taget_second_array, ANTI_CLOCK_WISE_90) # 반시계방향 90도
    print(f"anti_clock_90 : \n", anti_clock_90)

    anti_clock_180 = np.rot90(roll_taget_second_array, ANTI_CLOCK_WISE_180) # 반시계방향 180도
    print(f"anti_clock_180 : \n", anti_clock_180)

    anti_clock_270 = np.rot90(roll_taget_second_array, ANTI_CLOCK_WISE_270) # 반시계방향 270도
    print(f"anti_clock_270 : \n", anti_clock_270)

    anti_clock_360 = np.rot90(roll_taget_second_array, ANTI_CLOCK_WISE_360) # 반시계방향 360도
    print(f"anti_clock_360 : \n", anti_clock_360)

    print("--- END rotate_second_array ---")
    return anti_clock_90


def reverse_second_array():
    print("--- BEGIN reverse_second_array ---")
    REVERSE_STEP = 1
    second_array = [[1,2,3],
                   [4,5,6],
                   [7,8,0]]
    second_array = np.array(second_array)
    print("reverse target :\n", second_array)
    print("reverse results :\n",second_array[::-REVERSE_STEP])
    print("--- END reverse_second_array ---")
    return second_array

# print("reverse results :\n", np.flip(second_array, 1))
def array_concat_array():
    print("--- BEGIN array_concat_array ---")
    cross = [
        [[3, 0, 1, 1, 8],
         [5, 0, 4, 5, 4],
         [1, 5, 0, 5, 1],
         [1, 2, 1, 0, 1],
         [0, 2, 5, 1, 1]],
        [[1, 2, 0, 3, 3],
         [1, 2, 0, 3, 3],
         [1, 2, 0, 2, 4],
         [4, 2, 0, 0, 1],
         [8, 4, 1, 1, 0], ]
    ]

    first_cross = cross[0]
    second_cross = cross[1]
    concat_cross = np.concatenate((first_cross, second_cross), axis=0)
    print("--- END array_concat_array ---")
    return concat_cross


def slicing_second_array():
    print("--- BEGIN slicing_second_array ---")
    second_array = [[1,2,3],
                   [4,5,6],
                   [7,8,0]]

    ROW_BEGIN = 2
    ROW_END = ROW_BEGIN + 2 # 최종 포함 행은 마지막 값에서 -1
    COLUMN_BEGIN = 1
    COLUMN_END = COLUMN_BEGIN + 2 # 최종 포함 열은 마지막 값에서 -1
    sliced_array = second_array[ROW_BEGIN:ROW_END, COLUMN_BEGIN:COLUMN_END]
    print("--- END slicing_second_array ---")
    return sliced_array

def flip_array():
    print("--- BEGIN flip_array ---")
    ROW = 0 # 위 아래 반전
    COLUMN = 1 # 좌우 반전
    second_array = [[1,2,3],
                   [4,5,6],
                   [7,8,0]]
    second_array = np.array(second_array)
    flipped_array = np.flip(second_array, COLUMN)
    print("reverse results :\n", flipped_array)
    print("--- END flip_array ---")
    return flipped_array

if __name__ == "__main__":
    print_second_list()
    print_enumerate_second_list()
    print("PADDING_VALUE : \n", padding_numpy())
    print("empty_list_by_np : \n", create_second_empty_list_by_np())
    print("empty_list_by_list : \n", create_second_empty_list_by_list())
    print("right_roll_second_array : \n", roll_second_array())
    print(f"rotate_second_array_90_degree : \n", rotate_second_array())
    print("reverse results :\n", reverse_second_array())
    print("array_concat_array :\n", array_concat_array())
    print("slicing_second_array :\n", slicing_second_array())
    print("flip_array :\n", flip_array())
