import sys
from collections import Counter

input = sys.stdin.readline

N = int(input())

numbers = []
for _ in range(N):
    numbers.append(int(input()))

# 산술평균
print(int(round((sum(numbers) / N), 0)))

# 중앙값
numbers.sort()
middle = (N // 2)
print(numbers[middle])

# 최빈값
# 최빈 횟수 구하기
counter = Counter(numbers)
mx_cnt = max(counter.values())
# 최빈값들
can = [num for num, cnt in counter.items() if cnt == mx_cnt]
# 정렬
can.sort()
if len(can) == 1:
    print(can[0])
else:
    print(can[1])

# 범위
if len(numbers) == 1:
    print(0)
else:
    print(max(numbers) - min(numbers))