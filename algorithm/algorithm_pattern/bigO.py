"""
시간 복잡도 초과시 딕셔너리로 전환하는 방법
- AS-IS : "if board[each_row][each_column] in nums"는 시간복잡도가 O(n)이다.
- TO-BE : "nums = set(nums)"을 사용하면 시간복잡도가 O(1)으로 줄어든다.
"""


def change_to_dict(board, nums):

    N = len(board)
    empty_list = [[0] * N for __ in range(N)] # 불필요한 함수 삭제

    nums = set(nums)

    for each_row in range(N):
        for each_column in range(N):
            if board[each_row][each_column] in nums:
                empty_list[each_row][each_column] = 1
