"""리스트 정렬시 사용
Reverse=True이면 내림 차순, 10-9-8
Reverse=False이면 오름 차순, 1-2-3

https://stackoverflow.com/questions/37693373/how-to-sort-a-list-with-two-keys-but-one-in-reverse-order
"""
from operator import itemgetter, attrgetter


class Student:

    def __init__(self, name, grade, age):
        self.name = name
        self.grade = grade
        self.age = age

    def __repr__(self):
        return repr((self.name, self.grade, self.age))


student_tuples = [
                ('john', 'A', 15),
                ('jane', 'B', 12),
                ('dave', 'B', 10),
            ]

student_objects = [
        Student('john', 'A', 15),
        Student('jane', 'B', 12),
        Student('dave', 'B', 10),
    ]

print("람다 이용 정렬", sorted(student_tuples, key=lambda x: x[0]))

print("문자열 길이 이용해 정렬", sorted(student_tuples, key=len))

print("2번째 요소 정렬", sorted(student_tuples, key=itemgetter(2)))

print("키값 'age'로 정렬", sorted(student_objects, key=attrgetter('age')))

print("키값 1번 기준으로 정렬한 뒤 정렬된 값에서 2번 기준으로 정렬로 정렬", sorted(student_tuples, key=itemgetter(1,2)))

print("키값 grade 기준으로 정렬한 뒤 정렬된 값에서 age 기준으로 정렬로 정렬", sorted(student_objects, key=attrgetter('grade', 'age')))

reversed_cross = sorted(student_tuples, key=itemgetter(2), reverse=True)
print("2번째 요소 역순으로 정렬", reversed_cross)

sortedList = sorted(myList, key = lambda y: (y[0].lower(), -y[1]))

def roll(d, n):
    """n칸씩 옆으로 이동"""
    print("--- BEGIN roll ---")
    print("before_roll : ", d)
    d.rotate(n)
    print(f"after_roll {n}: ", d)
    print("--- END roll ---")
    return d