"""
+ 덧셈

- 뺄셈

* 곱하기

** 거듭 제곱

/ 나누기

// 나누기 연산 후 소수점 이하의 수를 버리고, 정수 부분의 수만 구함

% 나누기 연산 후 몫이 아닌 나머지를 구함
"""


def op_double_division():
    """//를 쓰면 몫만 구할 수 있다. int로 전환하지 않아도 된다."""
    length_list = [1, 2, 3, 4, 5]
    # as-is
    total_length = int(len(length_list)/2)
    print(total_length)
    # to-be
    total_length = len(length_list) // 2
    print(total_length)