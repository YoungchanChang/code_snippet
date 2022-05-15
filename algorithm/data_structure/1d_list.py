"""리스트 CRUD경우에 사용
- 리스트 삽입 메소드 : insert_to_list()
- 리스트 삭제 메소드 : delete_to_list()
- 리스트에서 특정 값 숫자셀 때 사용 : list_count()
  - 모든 값을 위해서는 데이터_개수_관리.py 참조
- 리스트 확장 시 사용 : list_extend()
- 리스트에서 값을 통한 인덱스 찾을 때 사용 : get_index_from_list()
- n번째 요소 삭제할 때 사용 : delete_nth(d, n)
ref : https://docs.python.org/3/tutorial/datastructures.html
"""
from collections import deque


def list_copy():
    lock = [[], [], []]
    _lock = [item[:] for item in lock]


def list_contain_list():
    """리스트 안에 다른 리스트가 포함됬는지 확인하는 함수"""
    big = []
    small = []
    result = all(elem in big for elem in small) # To check if big contains ALL elements in small
    result = any(elem in big for elem in small) # To check if small contains ANY elements in big

def list_to_dict():
    """2차원 리스트에 2개의 데이터가 쌍으로 있으면 dictionary형으로 바로 변환할 수 있다."""
    specs = [['toy', '70'], ['snack', '200']]

    # AS-IS
    spec_dict = dict()
    for spec in specs:
        spec_dict[spec[0]] = int(spec[1])

    # TO-BE
    spec_dict = dict(specs)  # 리스트르를 dict()로 전환


def insert_to_list():
    print("--- BEGIN insert_to_list ---")
    test_list = [1, 2, 3, 4, 5]
    append_value = 9
    test_list.append(append_value)
    print(f"append : {append_value}", test_list, id(append_value))

    insert_idx = 2
    insert_value = 22
    test_list.insert(insert_idx, insert_value)
    print(f"insert_idx : {insert_idx}, insert_value : {insert_value},", test_list, id(insert_value))
    print("--- END insert_to_list ---")


def delete_to_list():
    print("--- BEGIN delete_to_list ---")
    """
    pop() - given position in the list, and return it
    remove() - value is equal to x. It raises a ValueError
    :return:
    """
    test_list = [1, 2, 3, 4, 5]
    pop_value = test_list.pop()
    print(f"pop_value : {pop_value},", test_list, id(test_list))
    pop_idx = 2
    pop_value = test_list.pop(pop_idx)
    print(f"pop_idx : {pop_idx}, pop_value : {pop_value},", test_list, id(test_list))
    print(test_list)

    remove_value = 4
    test_list.remove(remove_value)
    print(f"remove value : {remove_value}, remove_result :",test_list, id(test_list))

    del_idx = 1
    del test_list[del_idx]
    print(f"delete idx : {del_idx}, remove_result :", test_list, id(test_list))
    print("--- END delete_to_list ---")


def list_count():
    print("--- BEGIN list_count ---")
    test_list = [1, 2, 3, 3, 3, 3, 4, 5]
    count_val = 3
    print(f"test_list", test_list)
    print(f"count_value : {count_val}", "count_number :", test_list.count(count_val))
    print("--- END list_count ---")


def list_extend():
    print("--- BEGIN list_extend ---")
    test_list = [1, 2, 3, 3, 3, 3, 4, 5]
    extend_list = [6, 7, 8]
    print("extend_list", extend_list)
    test_list.extend(extend_list)
    print("after_extend_results", test_list)
    print("--- END list_extend ---")


def get_index_from_list():
    print("--- BEGIN get_index_from_list ---")
    test_list = [1, 2, 3, 3, 3, 3, 4, 5]
    index_value = 3
    print(f"index_value : {index_value}, index :",test_list.index(index_value))
    print("--- END get_index_from_list ---")


def delete_nth(d, n):
    """리스트에서 n번째 삽입삭제"""
    print("--- BEGIN delete_nth ---")
    d.rotate(-n)
    print(f"rotate -{n}", d, id(d))
    d.popleft()
    print("popleft", d, id(d))
    d.rotate(n)
    print(f"rotate {n}", d, id(d))
    print("--- END delete_nth ---")


if __name__ == "__main__":
    iterable_list = ['ABC', 'D', 'EF', "FGH", "DEFAB"]
    iterable_deque = deque(iterable_list)
    del iterable_deque[3]
    print("iterable_deque", iterable_deque)
    delete_nth(iterable_deque, 3)
    insert_to_list()
    delete_to_list()
    list_count()
    list_extend()
    get_index_from_list()