# 입력
# N개의 수 A, B
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

B.sort()
A.sort(reverse=True)

sum = 0

for i in range(N):
    sum += A[i] * B[i]

print(sum)