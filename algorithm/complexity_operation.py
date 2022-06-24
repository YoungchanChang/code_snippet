"""리스트와 딕셔너리의 시간, 공간복잡도 테스트

- ref:
  - https://docs.python.org/3/library/sys.html
  - https://www.ics.uci.edu/~pattis/ICS-33/lectures/complexitypython.txt
  - https://wiki.python.org/moin/TimeComplexity
  - https://stackoverflow.com/questions/6529966/what-is-the-space-complexity-of-a-hash-table
"""
import time

import sys
# 1. 빈 딕셔너리와 리스트를 생성합니다.
dictionary_object = dict()
dictionary_size = sys.getsizeof(dictionary_object)
list_object = list()
list_size = sys.getsizeof(list_object)
print(f"size of dictionary object : {dictionary_size} bytes")
print(f"size of list object : {list_size} bytes")


list_object.append("장영찬")
print(list_object)
list_object.append("김영희")
print(list_object)
list_object.insert(1, "김철수")
print(list_object)

print(list_object.index("김철수"))


# 2. 딕셔너리와 리스트에 값을 삽입하고 공간 복잡도를 확인합니다.
limit = 10000000
for x in range(0, limit, 1):
    dictionary_object[x] = x
    list_object.append(x)
dictionary_size = sys.getsizeof(dictionary_object)
list_size = sys.getsizeof(list_object)
print(f"size of dictionary object, key range from 0 to {limit} : {dictionary_size} bytes")
print(f"size of list object, range from 0 to {limit} : {list_size} bytes")
print(f"space efficient : {round(dictionary_size/list_size, 5)}")


# 3. 딕셔너리와 리스트에 값을 검색 후에 시간 복잡도를 확인합니다.
search_value = limit-1
st = time.perf_counter()
print("found_value of dictionary object : ", dictionary_object.get(search_value, None))
dictionary_search_costs = time.perf_counter() - st
print(f"search_time costs : {dictionary_search_costs}")

st = time.perf_counter()
print("found_value of list object : ",list_object.index(limit - 1))
list_search_costs = time.perf_counter() - st
print(f"search_time costs : {list_search_costs}")

print(f"time efficient : {round(list_search_costs/dictionary_search_costs, 5)}")
