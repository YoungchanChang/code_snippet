"""데이터 정렬시 필요

주어진 데이터가 2차원 형태의 테이블일 때 사용

- 키값에 따라서 값을 추가해야 될 때 사용 : group_by_default_dict()
- 1차원 배열 묶을 때 사용 : group_by_1_array()
- 2차원 배열 묶을 때 사용 (합을 구할 수 있다.) : group_by_2_array()

ref : https://docs.python.org/ko/3/library/itertools.html
ref : https://kimdoky.github.io/python/2019/11/24/python-itertools/
"""
import itertools
from collections import defaultdict


def group_by_default_dict() -> dict:
	print("--- BEGIN group_by_default_dict_list ---")
	saving_list = [
		('item1', 55),
		('item2', 75),
		('item3', 15),
		('item4', 6)
	]

	saving_dict = defaultdict(list)
	for item, number in saving_list:
		if number < 10:
			saving_dict['not_expensive'].append(item)
		elif number < 50:
			saving_dict['can_buy'].append(item)
		else:
			saving_dict['expensive'].append(item)
	print("--- END group_by_default_dict_list ---")
	return saving_dict



def group_by_1_array():
	print("--- BEGIN group_by_1_array ---")
	string_target = 'AAABBBCCDAABBB'
	group_by_string_target = [(k, list(g)) for k, g in itertools.groupby(string_target)]
	print("group_by_string_target", group_by_string_target)

	sorted_target = sorted(string_target)
	group_by_sorted_target = [(k, list(g)) for k, g in itertools.groupby(sorted_target)]
	print("group_by_sorted_target",  group_by_sorted_target)
	print("--- END group_by_1_array ---")


def group_by_2_array():
	print("--- BEGIN group_by_3_array ---")
	SORT_KEY = 0
	SUM_KEY = 1
	SUM_SECOND_KEY = 2
	spend_money = [ ('ho', 10000, 100),
					('jung', 2000, 200),
					('gil', 200, 300),
					('dong', 100, 400),
					('ho', 1000, 500),
					('gil', 20, 600)
					]

	spend_money = sorted(spend_money, key=lambda x: x[SORT_KEY])
	print(list(itertools.groupby(spend_money)))

	for name, money in itertools.groupby(spend_money, lambda x: x[SORT_KEY]):
		money = [i for i in money]
		print(f'{name} SUM_KEY : {sum([i[SUM_KEY] for i in money])}')
		print(f'{name} SUM_SECOND_KEY : {sum([i[SUM_SECOND_KEY] for i in money])}')
	print("--- END group_by_3_array ---")


if __name__ == "__main__":
	print("group_by_list() :", group_by_default_dict())
	print("group_by_1_array() :", group_by_1_array())
	print("group_by_2_array() :", group_by_2_array())
