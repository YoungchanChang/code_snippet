
# One main difference is while loops are best suited when you do not know ahead of time the number of iterations that you need to do.
# When you know this before entering the loop you can use for loop.


# 반복이 언제 끝날지 모르면, while문을 쓰는 것이 좋다.
# 시작점, 끝점, 증가의 조건를 모를 때 쓰면 좋다.
# 조건문이 변하는 경우, while문을 쓰면 좋다.
# 반복이 언제 끝날지 알면 for문을 쓰는 것이 좋다
# - 'while문`에 비해 `가독성`이 증가한다.
# - 시작점, 끝점, 증가의 조건을 알 때 쓰면 좋다.
# 리스트나 문자열 같은 시퀀스가 주어졌을 때 쓰면 좋다.
#

# while문을 쓰면 좋은 상황
# 조건문이 입력값에 따라 변한다.
number = 0

while number != 4:  # Do this until number becomes four
    number = int(input())
    print(f"your number input is {number}")



# while문을 쓰면 좋은 상황 2
# 딕셔너리의 값이 다른 키값을 참조할 때 쓰인다.
hash_dict = {
    "A" : "B",
    "B" : "C",
    "C" : "D"
}

key = "A"
key_find = key
hash_end = None
while (hash_value := hash_dict.get(key_find, None)):  # Do this until number becomes four
    hash_end = hash_value
    key_find = hash_value
print(f"key {key}'s value is {hash_end}")

# for문을 쓰면 좋은 경우
# 숫자의 범위가 주어졌을 때 활용한다.
for i in range(5, 8, 1):
    print(f"value of range is {i}")

# for문을 쓰면 좋은 경우 2
# 시퀀스 자료의 순서를 제어하고 싶을 때 enumerate()와 사용한다.

for idx, i in enumerate(range(5, 9, 1)):
    print(f"index number is {idx}'s value is {i} ")

