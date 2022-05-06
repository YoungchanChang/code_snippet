"""
- 최고점을 찾는 문제에 활용
https://docs.python.org/ko/3/library/heapq.html

# max heap구현 방법
1. 음수 붙이기
- 1-1) 처음부터 음수로 정렬한 뒤 heap하기
works = [-i for i in works] # max heap
heapify(works)
- 1-2) 푸쉬할 때 음수로 넣고 출력할 때 음수로 출력하기
heapq.heappush(hq, -1)
print(-heapq.heappop(hq))

2. 튜플 사용
- 가장 첫번째 입력을 기준으로 정렬한다.
heapq.heappush(hq, (-1, 1)
heapq.heappop(hq)[1]
"""


from heapq import heapify, heappush, heappop, heapreplace


def push_pop_heap(input_list, input_K):
    heapify(input_list) # 정렬
    count = 0

    while input_list[0] < input_K:
        try:
            heappush(input_list, heappop(input_list) + heappop(input_list) * 2)
        except IndexError:
            return -1
        count += 1

    return count


def max_heap(no, works):
    if no > sum(works):
        return 0

    # 1. 처음부터 음수로 정렬하기
    works = [-i for i in works] # max heap
    heapify(works)

    # 2. 조건에 따라 heapreplace 진행하기
    for _ in range(no):
        heapreplace(works, works[0] + 1)
        # heappushpop 먼저 푸시하고 팝
        # heapreplace 먼저 팝하고 푸시

    return sum([i ** 2 for i in works])


if __name__ == "__main__":

    test_list = [0, 9, 8 , 3, 7, 6, 1]
