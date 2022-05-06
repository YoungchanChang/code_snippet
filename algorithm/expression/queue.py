"""
# queue와 list의 차이
queue와 list의 가장 큰 차이는 첫번째 원소를 추출하는 방식이다.
queue는 popleft()메소드를 사용하여 시간복잡도가 O(1)으로 완료될 수 있다.
반면, list는 O(N)의 시간 복잡도가 든다.

# queue의 사용
popleft()에 첫 원소가 추출되는 기능을 응용하여 첫번째 원소의 순서를 추출하는 로직에 사용할 수 있다.
"""

from collections import deque


def get_que_template():
    image_que = deque(image)

    while image_que:
        image_que_item = image_que.popleft() # 큐를 하나 뽑는다.

        if image_que_item < 1: # 큐에 조건문을 건다.
            image_que.append(image_que_item) # 큐에 조건을 추가한다.


if __name__ == "__main__":
    image = [0, 1, 2]
    get_que_template()