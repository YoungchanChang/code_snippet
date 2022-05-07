import itertools


# zip으로 묶을 때, 빈 값 사용
print(list(itertools.zip_longest('ABCD', 'xy', fillvalue='-')))

# 순열과 조합.
# 중첩된 for 루프
print(list(itertools.product('ABCD', repeat=3)))

# 순열 - 중복 허용
print(list(itertools.permutations('ABCD', 2)))

# 조합- 앞과 뒤가 다른 것 허용 X
print(list(itertools.combinations('ABCD', 2)))

print(list(itertools.combinations_with_replacement('ABCD', 2))) # 이 리스트 중에 2개만 선택하는 겨우

z = list(itertools.combinations_with_replacement('ABCD', 2))

# 순열 조합 Counter 콤비네이션 => 특정한 요소들의 개수를 셀 수 있다.

from collections import Counter
ttt = list(itertools.permutations('ABCD', 2))

my_list = ['i', 'love', 'chicken', 'tender', 'you', 'love', 'i']

print(Counter(list(itertools.permutations(my_list, 2))))

print(ttt)
print(Counter(ttt))
print(Counter(z))

print(list(itertools.permutations([86, 58, 29], 2)))
print(list(itertools.permutations([[0,1,2,3], [7,8,9], ["Z","B","C"]], 2)))

def find_permutations(begin_sequences, full_set):
    for begin_sequence in begin_sequences:
        remaining_set = full_set - set(begin_sequence)
        for ending in itertools.permutations(remaining_set):
            yield begin_sequence + list(ending)
full_set = set(range(1,37))
# A에서 5, 1, 2중에 하나 선택
# B에서 5, 1, 6중에 하나 선택
# C에서 ["Z","B","C"]하나 선택
# for p in find_permutations([[5,1,2], [5,1,6], [5,1,7]], full_set):
#     print(p)