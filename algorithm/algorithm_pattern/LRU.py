"""
특정 값 발견시, 가장 먼저 앞에 오게할 때
딕셔너리 순서 재배치에 특화된 메서드
"""
from collections import OrderedDict


def get_ordered_dict():
    oneDict = {'one': 1, 'two': 2, 'three': 3}
    d = OrderedDict(oneDict)

    print(d) # OrderedDict([('one', 1), ('two', 2), ('three', 3)])

    d.move_to_end('two') # 맨 앞이나 맨 뒤로 보낼 때 사용
    print(d) # OrderedDict([('one', 1), ('three', 3), ('two', 2)])

    d.move_to_end('two', False)
    print(d) # OrderedDict([('two', 2), ('one', 1), ('three', 3)])
    print(d.get('two'))
    d['two'] +=1
    print(d)

    # 옵션값 True가 디폴트. d.popitem(True) == d.popitem()
    print(d.popitem(True)) # 맨 뒤에서 딕셔너리 뽑음
    # # ('three', 3)

    print(d.popitem(False)) # 맨 앞에서 딕셔너리 출력
    # ('two', 2)
    print(d) # OrderedDict([('one', 1)])



class LastUpdatedOrderedDict(OrderedDict):
    'Store items in the order the keys were last added'

    def __setitem__(self, key, value):
        super().__setitem__(key, value)
        self.move_to_end(key)

last_update_dict = LastUpdatedOrderedDict()
last_update_dict[5] = 3
last_update_dict[6] = 2
last_update_dict[7] = 2
last_update_dict[8] = 9
print("before add : ", last_update_dict)
last_update_dict[5] += 1
print("after add : ", last_update_dict)
print("pop last value : ", last_update_dict.popitem(last=True), last_update_dict)
print("pop first value : ", last_update_dict.popitem(last=False), last_update_dict)
