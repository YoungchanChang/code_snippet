"""

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