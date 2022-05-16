# 자료구조

- 자료구조에서 중요하게 보아야 할 부분
- 메모리 저장 구조
- 시간복잡도

# 자료구조 목차
1. Array & Linked List
- 고대 면접에서 옆 아저씨한테 질문했던 기억 난다.

2. Queue & Stack

3. Hash table & BST(Binary Search Tree) 

# 내용
1. Array & Linked List

- 핵심 : Array는 메모리상에서 연속적으로 데이터를 저장하고, Linked List는 불연속적으로 저장
- 조회 (lookup) : Array에 강점
- 삽입/삭제 (insert/delete) : Linked List에 강점
- 메모리 낭비

## Array
- 메모리
  - 고정된 저장 공간(fixed-size)
  - 순차적인 데이터 저장(order)
  - Stack영역 
- 시간복잡도
  - `access, append` O(1)

## Dynamic array
- 메모리 : resize
  - resize방식 : Doubling
  - O(n)으로 일일이 옮긴다
* amortized O(1) : 최악수행시간분석


## Linked List
- 메모리
  - Node 구조체(데이터 값과 다음 Node의 address를 저장)
  - 논리적인 연속성, 물리적인 메모리상에서는 비연속적
  - Heap영역
- `insert, remove` : O(1)

2. Queue & Stack
## Queue
- 메모리
  - FIFO(First In First Out)

- 시간복잡도
  - 리스트와 같음. Popleft()일 시 O(1)
  - enqueue와 dequeue는 모두 O(1)의 시간복잡도

- 사례
  - 데이터베이스 요청, CPU task scheduling, BFS 알고리즘 등에 사용

## Stack
- 메모리
  - LIFO(Last In First Out)
- 시간복잡도
  - push & pop O(1)

* Queue * Priority Queue
# Priority Queue
Heap은 우선순위 큐를 구현하기 위한 방법이고 우선순위 큐는 개념
- 메모리
  - 우선순위가 높은 요소가 먼저 나가는 자료 구조
  - 요소가 삽입 될 때 바로 정렬

- 메모리
  - 시간복잡도 O(logn)

3. Hash table & BST(Binary Search Tree)

# BST(Binary Search Tree)
- 메모리
  - 저장과 동시에 정렬을 하는 자료구조
  - 해당 node의 left subtree에는 그 node의 값보다 작은 값들을 지닌 node들
  - node의 right subtree에는 그 node의 값보다 큰 값들을 지닌 node들

- 시간복잡도
  - 검색, 저장, 삭제 : O(logn)

* 최악의 복잡도를 방지하기 위한 방법
- 자가 균형 이진 탐색 트리(Self-Balancing BST)는 알고리즘으로 이진 트리의 균형이 잘 맞도록 유지하여 높이를 가능한 낮게 유지
- AVL트리, Red-black tree

# Hash table
- 메모리
  - 효율적인 탐색(빠른 탐색)을 위한 자료구조로써 key-value쌍의 데이터를 입력
- 시간복잡도
  - 저장, 삭제, 검색의 시간복잡도는 모두 O(1)
  - collision으로 인하여 최악의 경우  O(n)

* seperate chaining 또는 open addressing
- separete chaining 방식은 linked list를 이용하는 방식은 Python에서 defaultdict()와 유사
- 데이터가 저장되기 전에 미리 저장공간(slot, bucket)을 확보
- open addressing
  - Linear Probing(선형 조사법)& Quadratic Probing(이차 조사법) : 탐사이동폭이 같기 때문에 클러스터링 문제가 발생
  - Double Hashing(이중해시, 중복해시) :  클러스터링 문제가 발생하지 않도록 2개의 해시함수를 사용하는 방식, 하나는 최초의 해시값을 얻을 때 사용하고 또 다른 하나는 해시 충돌이 발생할 때 탐사 이동폭을 얻기 위해 사용



시간복잡도 참조
> https://wiki.python.org/moin/TimeComplexity