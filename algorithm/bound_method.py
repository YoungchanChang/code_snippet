"""
# 바운드 메서드
- 모든 인스턴스는 같은 함수를 공유한다.

바운드 메서드 내용 : https://docs.python.org/3/reference/datamodel.html
바운드 메서드 설명 - https://wikidocs.net/84418
바운드 메서드 실습 : https://stackoverflow.com/questions/66838841/instance-methods-sharing-in-python
getsizeof의 파이썬 도큐먼트: getsizeof
전역변수와 지역변수 : https://wikidocs.net/21060
멤버변수가 궁금하다면 : https://wikidocs.net/9665
추가로 읽으면 좋은 글 : https://scoutapm.com/blog/python-memory-management
"""
import sys


class B:

    def test(self):
        ...

    def test2(self):
        ...


class A:
    def __init__(self):
        self.B = B()


# 메모리 사이즈 계산
print(sys.getsizeof(A))
print(sys.getsizeof(B))


class MyData: # 전역변수로써
    def __init__(self, number):
        self.data = number

    def test(self):
        self.data2 = self.data

#
my_data1 = MyData(number=1) # 파이
print(sys.getsizeof(my_data1))
print(hex(id(my_data1)))
print(dir(my_data1))
#
my_data2 = MyData(number=2)
print(sys.getsizeof(my_data2))
print(hex(id(my_data2)))
print(dir(my_data2))
print(hex(id(MyData)))

print(hex(id(my_data2.test())))
print(hex(id(my_data2.test())))



class CCC(object):
    def __init__(self, color):
        print(f"id of self in __init__ on class is {hex(id(self))}")

    def test(self, color=None):
        print(f"hello {color}")
        print(f"id of __init__ on class is {hex(id(self))}")
    print(f"id of __init__ on class is {hex(id(__init__))}")
    def test2(self):
        ...


a = CCC("red")

print(hex(id(a.__init__))) # 그런데 a.__init__의 id값은 b.__init__의 값과 같다.
print("where you from?", hex(id(a.test)))
print("I am CCC", CCC)
print("I am CCC", CCC)
print("i am a", a)
zzz = a.__init__
print(zzz)
print("i am a.__init__", a.__init__)
print("where you from a?", a.test)
print("Hello!!!", CCC.test(a, "blue"))
b = CCC("green")
b.test()
print(hex(id(b.__init__)))
print("where you from b?", b.__init__)
print("where you from b?", b.test)
zzzzz = b.__init__
kkkkkk = b.test


print(dir(a))
print(dir(a.__class__))
print(a)
CCC.test(b, "red")
print(a)
print(CCC.__init__)
print(hex(id(CCC)))
print(hex(id(CCC.__dict__)))
print(hex(id(CCC.test)))
print(hex(id(CCC.test2)))
print(CCC)
