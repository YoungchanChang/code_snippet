import math


def DFS(current_depth, sum):
    """이전 데이터에서 넘어온 정보를 가지고 있다."""
    global result

    if result != -math.inf: # 결과값이 정해졌다면 모든 결정트리 취소
        return

    if current_depth == len(a): #인덱스의 마지막 값에 도달하면 검사
        print("SUM :", sum, "TOTAL :", total, "OTHER_SUM :", total-sum)

        other_sum = (total-sum) # 전체에서 내가 만든 부분집합을 제거한다.
        if sum == other_sum:
            result = sum
            print("YES")

    else: #인덱스 끝까지 가기 전까지
        print("current_depth :", current_depth, "sum :", sum, "current_value :", a[current_depth], "next_level :", current_depth + 1)
        DFS(current_depth + 1, sum + a[current_depth])
        print("current_depth :", current_depth, "sum :", sum, "current_value : SKIP", "next_level :", current_depth + 1)
        DFS(current_depth + 1, sum)


if __name__ == "__main__":
    n = 6
    a = [1, 3, 5, 6, 7, 10]
    result = -math.inf # 최종적으로 구하고자 하는 값
    total = sum(a)
    DFS(0, 0)

    limit = 0