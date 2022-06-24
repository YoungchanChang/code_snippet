"""딕셔너리 CRUD

- 리스트를 딕셔너리 안에 넣을 때 사용 : list_in_dictionary()
- 키값에 중복되는 값을 없을 때 사용 : group_by_set()
- 딕셔너리가 여러개일 때 사용 : concat_dictionary()
- 딕셔너리에서 키, 값, 아이템 읽을 때 사용 : read_dictionary()

ref : https://docs.python.org/3/tutorial/datastructures.html
"""
from collections import ChainMap
from collections import defaultdict


def list_in_dictionary():
    print("--- BEGIN list_in_dictionary ---")
    s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
    d = defaultdict(list)
    for k, v in s:
        d[k].append(v)
    print("--- END list_in_dictionary ---")
    return d


def set_in_dictionary():
    print("--- BEGIN set_in_dictionary ---")
    s = [('red', 1), ('blue', 2), ('red', 3), ('blue', 4), ('red', 1), ('blue', 4)]
    d = defaultdict(set)
    for k, v in s:
        d[k].add(v)

    sorted(d.items())
    print("--- END set_in_dictionary ---")
    return d


def concat_dictionary():
    print("--- BEGIN concat_dictionary ---")
    d = {
        'one' : 1,
        'two' : 2,
        'three' : 3
    }
    k = {
        'four' : 4
    }

    chain = ChainMap(d, k)
    print("key_chain", chain)
    print("key['one']", chain['one'], "key['four']", chain['four'])

    # 딕셔너리 위치를 이용한 적븐
    print("first_inserted_chain :", chain.maps[0]) # {'one': 1, 'two': 2, 'three': 3}
    print("second_inserted_chain :", chain.maps[1]) # {'four': 4}

    print("show_keys :", chain.keys()) # KeysView(ChainMap({'one': 1, 'two': 2, 'three': 3}, {'four': 4}))
    print("show_items_in_list :", chain.items())# ItemsView(ChainMap({'one': 1, 'two': 2, 'three': 3}, {'four': 4}))
    print("show_keys_in_list :", list(chain))  # KeysView(ChainMap({'one': 1, 'two': 2, 'three': 3}, {'four': 4}))
    d = chain.new_child(m={"hello": "world"})
    print("new_child_added", d)
    chain.update({"hello_second": "worlds"})
    chain["hello_third"] = "hello_third"
    print("add_data_in_two_way :", chain)
    print("--- END concat_dictionary ---")
    return chain


def read_dictionary():
    print("--- BEGIN read_dictionary ---")
    test_dictionary = {"a" : 1, "b" : 2, "c": 5}

    assert list(test_dictionary.keys()) == ['a', 'b', 'c']
    print(list(test_dictionary.keys()))

    assert list(test_dictionary.values()) == [1, 2, 5]
    print(list(test_dictionary.values()))

    assert list(test_dictionary.items()) == [('a', 1), ('b', 2), ('c', 5)]
    print(list(test_dictionary.items()))
    print("--- END read_dictionary ---")


if __name__ == "__main__":
    print(list_in_dictionary())
    print(set_in_dictionary())
    print(concat_dictionary())
    read_dictionary()

