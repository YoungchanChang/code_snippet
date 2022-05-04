"""
- 최고점을 찾는 문제에 활용
https://docs.python.org/ko/3/library/heapq.html

# max heap구현 방법
1. 음수 붙이기
heapq.heappush(hq, -1)
print(-heapq.heappop(hq))

2. 튜플 사용
heapq.heappush(hq, (-1, 1)
heapq.heappop(hq)[1]
"""
from heapq import heapify, heappop

if __name__ == "__main__":

    test_list = [0, 9, 8 , 3, 7, 6, 1]
    heapify(test_list) # heap 구조로 정렬
    print(test_list)
    lowest_val = heappop(test_list) # 가장 값이 낮은 데이터 추출
    print(lowest_val)
