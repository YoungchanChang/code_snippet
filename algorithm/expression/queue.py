from collections import deque

if __name__ == "__main__":
    image = [0, 1, 2]
    image_que = deque(image)
    tmp_que = []

    while image_que:
        image_que_item = image_que.popleft()
        print(image_que_item)