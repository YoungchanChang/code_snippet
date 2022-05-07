"""
힙큐 문제 유형
- 조건을 만족하는 가장 최대/최소값
- 실시간으로 정렬이 이루어져야 하는 경우
"""


from heapq import heapify, heappush, heappop, heapreplace


def heap_sort():

    heap_lst = [5, 1, 2, 7, 4, 9, 8, 10, 3, 6]
    heapify(heap_lst)  # lst를 Heap으로 정렬. 시간복잡도 O(log n).
    print(heap_lst)  # [1, 3, 2, 5, 4, 9, 8, 10, 7, 6] Heap 기준에서 바라볼 때 정렬된 모습

    heappush(heap_lst, 3)  # 3삽입 후 트리 정렬 시간복잡도 O(log n)
    print(heap_lst)  # [1, 3, 2, 5, 3, 9, 8, 10, 7, 6, 4]

    heappop(heap_lst)  # 가장 작은 값 1을 반환하고 제거. 재정렬에 O(log n)이 소요.
    print(heap_lst)  # [2, 3, 4, 5, 3, 9, 8, 10, 7, 6] 1 다음으로 작은 값인 2가 root로 선택.


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
    """
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

    heap_sort()