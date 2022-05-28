"""3차원 공간 정보를 다룰 때 쓰기 위한 메소드
ex) 길찾기 문제

- 좌표 정보를 담은 빈 리스트 생성 : create_third_empty_list_by_list()
- 시작점에서 다음 좌표를 따라 끝점까지 진행할 때 : following_coordinate()
- 시작점에서 다음 좌표를 따라 끝점까지 진행할 때 2 : following_step()
- 2차원 배열 순행하며 누적 계산 : column_forward()
- 2차원 배열 순행하며 누적 계산 : column_backward()

"""
import numpy as np

a = [
    [[1, 2], [2, 3]],
    [[3, 4], [4, 5]],
    [[5, 6], [6, 7]]
    ]

print("행에 대한 정보 : ", a[0])
print("열에 대한 정보 : ", a[0][0])
print("좌표값에 대한 정보 : ", a[0][0][0])


def create_third_empty_list_by_list(row=3, column=5) -> list:
    print("--- BEGIN create_third_empty_list_by_list ---")
    empty_list = [[[0, 0, 0] for _column in range(column)] for _row in range(row)]
    print("row_num :", row, "column_num :", column, "\n", empty_list)
    print("--- END create_third_empty_list_by_list ---")
    return empty_list


def following_coordinate():
    print("--- BEGIN following_coordinate ---")
    empty_list = [[[0, 1], [0, 2], [1, 2]],
                  [[1, 0], [0, 2], [2, 2]],
                  [[1, 0], [0, 2], [3, 3]],
                  ]
    coordinate = []
    x = 0 # start
    y = 0 # start
    coordinate.append((x,y))
    X_END = 3
    Y_END = 3

    X_COORD = 0
    Y_COORD = 1
    cnt = 0

    # x, y의 좌표가 최종 목적지일 때까지 반복
    while not ((x == X_END) and (y == Y_END)):
        x, y = empty_list[x][y][X_COORD], empty_list[x][y][Y_COORD]
        # y = 포맷으로 하면 바로 윗줄 영향
        coordinate.append((x, y))
        if cnt == 100:
            raise Exception("Preventing infitie loop")
    print("--- END following_coordinate ---")
    return coordinate

cross = [
    [[3, 0, 1, 1, 8],
     [5, 0, 4, 5, 4],
     [1, 5, 0, 5, 1],
     [1, 2, 1, 0, 1],
     [0, 2, 5, 1, 1]],
    [[1, 2, 0, 3, 3],
     [1, 2, 0, 2, 4],
     [1, 2, 0, 2, 4],
     [4, 2, 0, 0, 1],
     [8, 4, 1, 1, 0], ]
]

first_cross = cross[0]
second_cross = cross[1]
cross_ = first_cross + second_cross

concat_cross = np.concatenate((first_cross, second_cross), axis=0).tolist()

가중치누적값 = [[0 for i in range(5)] for i in range(len(cross_))]
좌표저장 = [[[0, 0] for i in range(5)] for j in range(len(cross_))]

def column_forward():
    for i in range(5):
        for j in range(5):
            if i==0 and j == 0:
                가중치누적값[0][0] = cross_[0][0]
                좌표저장[i][j] = i, j
            elif i==0:
                가중치누적값[i][j] = 가중치누적값[i][j-1] + cross_[i][j]
                좌표저장[i][j] = i, j-1
            elif j == 0:
                가중치누적값[i][j] = 가중치누적값[i-1][j] + cross_[i][j]
                좌표저장[i][j] = i-1, j
            else:
                # 가중치누적값[i][j] = min(가중치누적값[i][j-1], 가중치누적값[i-1][j]) + cross_[i][j]
                if 가중치누적값[i][j-1] > 가중치누적값[i-1][j]:
                    가중치누적값[i][j] = 가중치누적값[i - 1][j] + cross_[i][j]
                    좌표저장[i][j] = i - 1, j
                else:
                    가중치누적값[i][j] = 가중치누적값[i][j - 1] + cross_[i][j]
                    좌표저장[i][j] = i, j - 1

    print(가중치누적값)
    print(좌표저장)

def column_backward():
    for i in range(len(cross_)):
        for j in range(4, -1, -1):
            if i==0 and j == 4:
                가중치누적값[0][4] = cross_[0][4]
                좌표저장[i][j] = [99, 99]
            elif i==0:
                가중치누적값[i][j] = 가중치누적값[i][j+1] + cross_[i][j]
                좌표저장[i][j] = i, j+1
            elif j == 4:
                가중치누적값[i][j] = 가중치누적값[i-1][j] + cross_[i][j]
                좌표저장[i][j] = i-1, j
            else:

                if 가중치누적값[i][j+1] > 가중치누적값[i-1][j]:
                    가중치누적값[i][j] = 가중치누적값[i - 1][j] + cross_[i][j]
                    좌표저장[i][j] = i - 1, j
                else:
                    가중치누적값[i][j] = 가중치누적값[i][j + 1] + cross_[i][j]
                    좌표저장[i][j] = i, j + 1


def following_step():
    k = 0
    while True:
        if k == 0:
            i, j = 좌표저장[len(cross_)-1][0]
        else:
            i, j = 좌표저장[i][j]
        if i == 99 and j == 99:
            break
        k += 1
        print(i, j)


if __name__ == "__main__":
    print(create_third_empty_list_by_list())
    print(following_coordinate())