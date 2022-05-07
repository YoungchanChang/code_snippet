"""
메모이제이션 기법
- DFS의 변형
- 배열의 이전 상태를 저장하고, 새로운 값을 생성한다.
"""


def DFS(len):

    if dy[len] > 0: # 여기가 핵심. 이미 기억하고 있는 정보는 더 이상 수행할 필요가 없다.
        return dy[len]

    if len==1 or len==2:
        return len

    else:
        dy[len] = DFS(len-1) + DFS(len-2)
        return dy[len]




if __name__ == "__main__":
    n = 5
    dy = [0] * (n+1)
    print(DFS(n))