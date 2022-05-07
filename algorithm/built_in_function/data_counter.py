"""
데이터에서 데이터의 개수를 구할 때 사용

- 데이터 수량중 덧셈, 뺄셈, 교집합, 합집합
- 데이터 총 개수, 가장 많은 원소의 개수, 가장 적은 원소의 개수
- https://docs.python.org/ko/3/library/collections.html
"""

from collections import Counter, defaultdict


def arithmetic_counter():
    print("--- BEGIN arithmetic_counter ---")

    save_list = {'one': 100, 'two': 200, 'three': 300}
    save_counter = Counter(save_list)
    print("save_counter :", save_counter)

    subtract_target = {'one': 20, 'two': 30}
    save_counter -= subtract_target
    print("subtract_target :", subtract_target)
    print("subtract_result :", save_counter)

    update_target = {'one': 1, 'two': 2}
    save_counter += update_target
    print("update_target :", update_target)
    print("update_result :", save_counter)

    intersect_target = {'one': 1, 'two': 2000}
    intersect_value = save_counter & Counter(intersect_target)
    print("intersect_target :", update_target)
    print("intersect_result :", intersect_value)


    union_target = {'one': 1, 'two': 2000, 'five': 30}
    union_value = save_counter & Counter(union_target)
    print("union_target :", union_target)
    print("union_result :", union_value)

    print("--- END arithmetic_counter ---")
    return save_counter


def count_from_list():
    print("--- BEGIN count_from_list ---")
    saving_list = [9, 1, 1, 2, 3, 4, 5, 5, 5, 6, 7, 9, 9, 9]
    saving_counter = Counter(saving_list)

    print("Counter info :", saving_counter)

    print("Counter total count info :", sum([x for x in saving_counter.values()]))
    # saving_counter.total() starts at 3.10 version

    print("Counter elements info : ",list(saving_counter.elements()))

    print("Counter keys-values of key info : ", list(saving_counter.keys()))
    print("Counter keys-values of count info : ", list(saving_counter.values()))

    print("Counter keys-values of items info : ", list(saving_counter.items()))
    print("Counter most_common info : ", saving_counter.most_common(3))
    print("Counter most_common backward info : ", saving_counter.most_common()[:-4:-1])
    print("--- END count_from_list ---")


def count_nlp():
    print("--- BEGIN count_nlp ---")
    my_list = ["한국", "에는", "어떤", "음식"]
    print("count by token :", Counter(my_list))

    s = '한국에는 어떤 음식이 있을까'
    d = defaultdict(int)
    for k in s:
        d[k] += 1
    print("count by char :", sorted(d.items()))
    print("--- END count_nlp ---")

if __name__ == "__main__":
    arithmetic_counter()
    count_from_list()
    count_nlp()

