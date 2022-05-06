"""
Queue를 활용한 BFS

문제 유형 : bfs_direction
- 조건에 따라 모든 지점 방문하기
"""

from collections import deque
import math


def bfs_direction(row, column, bfs_array):
    """
    1. direction으로 상하좌우방향을 미리 만들어 놓는다.
    2. visit한 부분은 math.inf로 바꾸어 놓는다.
      - visited = np.zeros((row, column), dtype=int) 같이 빈 값으로 생성할 수 있다.
    3.  조건에 따라 방문 지점 설정
    """

    answer = 0
    directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]

    for sy in range(row):
        for sx in range(column):

            # 1. 백트래킹 - 방문 지점 미방문
            if bfs_array[sy][sx] == math.inf:
                continue

            # 2. 미방문 지점만 새로운 큐로 생성
            target_answer = bfs_array[sy][sx]
            queue = deque([(sy, sx)])

            # 3. 모든 지점 방문
            while queue:
                y, x = queue.popleft()

                # 3-1. 상하 좌우 모든 지점 방문
                for dy, dx in directions:
                    ny = y + dy
                    nx = x + dx

                    # 3-2. 재방문 조건 지정
                    if 0 <= nx < row and 0 <= ny < column and bfs_array[ny][nx] == target_answer:
                        bfs_array[ny][nx] = math.inf
                        queue.append((ny, nx))

            answer += 1

    return answer
