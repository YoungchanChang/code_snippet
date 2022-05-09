"""
get_even_data()
빵과 음료수같이 짝이 있는 문제에 사용.
음료수를 받았는데 빵을 못 받은 경우를 구할 때 사가

reverse_stack()
- 스택을 역순으로 접근
- 조건에 맞지 않으면 pop()
"""


def get_even_data(s):
    c = 0
    for x in s:
        if x == '빵':
            c += 1
        else:
            c -= 1
        if c < 0:
            return False
    return c == 0


def reverse_stack(s):
    stack = []

    for s_item in s:
        if stack == []: # 비어있으면 값 추가
            stack.append(s_item)
            continue

        for answer_idx in range(len(stack)-1, -1, -1): # 스택을 역순으로 접근
            if stack[answer_idx] < s_item:
                stack.pop() # 기준에 맞지 않는 stack()은 pop
            else:
                break

        stack.append(s_item)

    return "".join(stack)