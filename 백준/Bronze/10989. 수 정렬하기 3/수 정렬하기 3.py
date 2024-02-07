import sys

# 입력
# 수의 개수 N
N = int(sys.stdin.readline())

# 수의 최솟값

count = [0] * 10001

for i in range(N):
    N = int(sys.stdin.readline())
    count[N] += 1

for i in range(len(count)):
    if i != 0:
        for j in range(count[i]):
            print(i)