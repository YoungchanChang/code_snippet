"""리스트에 범위 설정할 때 활용

- 순차적으로 증가하는 범위 설정 : range_forward()
- 순차적으로 감소하는 범위 설정 : range_backward()
- 마지막 인덱스, 값 확인 : list_last_value()
- 특정 범위만큼 리스트에서 가져오고 싶을 때 : get_list_from_range()
- 인덱스에 index error막기 위해 최소값만 넣어야 할 때 : prevent_list_index_error()

https://stackoverflow.com/questions/7122535/python-ensuring-a-variable-holds-a-positive-number
"""


def range_step():
    N = 4
    for _ in range(N):
        ...


def range_forward():
    START = 0
    END = 4 # END is not inlclude
    STEP = 1
    print("range_forward :", list(range(START, END, STEP)))
    assert list(range(START, END, STEP)) == [0, 1, 2, 3]


def range_backward():
    START = 4
    END = 0 # END is not inlclude
    STEP = -1
    print("range_backward :", list(range(START, END, STEP)))
    assert list(range(START, END, STEP)) == [4, 3, 2, 1]


def list_last_value():
    test_list = [1, 2, 3, 4, 5, 6, 7]
    print(test_list)
    last_idx = len(test_list)-1
    print("last_value :", test_list[last_idx])
    print("last_value :", test_list[-1])


def get_list_from_range():
    test_list = [1, 2, 3, 4, 5, 6, 7]
    START = 4
    print(f"START_IDX : {START}, START_VAL :", test_list[START])
    limit_val = [test_list[x] for x in range(START, len(test_list), 1)]
    print(test_list[START:len(test_list):1])
    print(f"START_IDX : {START}, END_IDX : {len(test_list)-1}, START_TO_END_LIST :", limit_val)


def prevent_list_index_error():
    test_list = [1, 2, 3, 4, 5, 6, 7]

    # 최대 6 이상 방지
    value_compare = 9
    min_limit_value = 6
    value = min(min_limit_value, value_compare)
    print(test_list[value])

    # 최대 0이하되기 방지
    value_compare = -6
    max_limit_value = 0
    value = max(max_limit_value, value_compare)
    print(test_list[value])


if __name__ == "__main__":
    range_forward()
    range_backward()
    list_last_value()
    get_list_from_range()
    prevent_list_index_error()