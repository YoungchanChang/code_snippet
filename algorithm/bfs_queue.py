# A를 방문했다. => 근처 지점을 방문해야 한다.
# 핵심 변수 : 좌표정보(2차원 배열), 방문지점, 방문할 지점

from collections import deque
import numpy as np

image = [[1, 5], [1, 5], [4, 5], [5, 5]]

n = len(image)
m = len(image[0])

row = n
column = m
visited = np.zeros((n, m), dtype=int)
will_visit = deque([])
cnt = 0


for each_row in range(0, row, 1):
    for each_column in range(0, column, 1):
        if not visited[each_row][each_column]:  # 미방문 지점이면 추가
            will_visit.append((each_row, each_column, image[each_row][each_column]))
            cnt += 1  # 미방문 지점일 때만 색상 추가

        while will_visit: # while문으로 계속 방문
            visit_point = will_visit.popleft() # 방문할 지점

            row_idx, column_idx, value = visit_point

            if visited[row_idx][column_idx]:  # 백트래킹 : 방문한 지점은 방문하지 않는다.
                continue

            if image[row_idx][column_idx] == value: # 조건문에 따라 상하좌우 방문
                visited[row_idx][column_idx] = 1  # 같은 색상일 때만 처리
                if row_idx - 1 >= 0:
                    will_visit.append((row_idx - 1, column_idx, value))

                if row_idx + 1 < n:
                    will_visit.append((row_idx + 1, column_idx, value))

                if column_idx - 1 >= 0:
                    will_visit.append((row_idx, column_idx - 1, value))

                if column_idx + 1 < m:
                    will_visit.append((row_idx, column_idx + 1, value))
