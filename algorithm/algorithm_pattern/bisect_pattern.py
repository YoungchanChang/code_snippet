"""
https://programming119.tistory.com/196
"""
from bisect import bisect_left, bisect_right


target_point = 32

number_data = [23, 87, 65, 12, 57, 32, 99, 81]
number_data.sort()

left_position = 0
right_position = len(number_data) - 1

while left_position <= right_position:
    middle_position = (left_position + right_position) // 2
    if number_data[middle_position] == target_point:
        print(middle_position + 1) # 0이 되지 않음으로
        break
    elif number_data[middle_position] > target_point:
        right_position = middle_position - 1
    else:
        left_position = middle_position + 1

nums = [2, 4, 4, 4, 6, 8, 10, 12, 14, 18, 20]
n = 4

print(bisect_left(nums, n))
print(bisect_right(nums, n))


def calCountsByRange(nums, left_value, right_value):
    r_i = bisect_right(nums, right_value)
    l_i = bisect_left(nums, left_value)
    return r_i - l_i

nums = [-1, -3, 5, 5, 4, 7, 1, 7, 2, 5, 6]
# 5 ~ 7 을 갖는 요소의 개수 구하기
nums.sort()
# 정렬은 필수
print(calCountsByRange(nums, 5, 7))


def decision_algorithm():
    k = 4
    n = 11
    Line = [802, 743, 457, 539]

    largest_line = max(Line)

    lt = 1
    rt = largest_line
    res = 0

    def count(len):
        cnt = 0
        for x in Line:
            cnt += (x // len)  # 라인에서 총 몇개의 라인이 만들어지냐
        return cnt

    while lt <= rt:
        mid = (lt + rt) // 2  # 중간값
        if count(mid) >= n:
            res = mid
            # 더 좋은 답을 찾아서
            lt = mid + 1
        else:
            rt = mid - 1

    print(res)

