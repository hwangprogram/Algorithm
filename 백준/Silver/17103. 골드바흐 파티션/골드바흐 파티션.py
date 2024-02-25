'''
# 17103 골드바흐 파티션

문제 요약
짝수 N이 주어졌을 때, 소수의 합으로 나타낼 수 있는 경우의 수를 구하여라
'''
import sys
input = sys.stdin.readline

# 에라토스테네스의 체
seive = [True] * (1000001)
primes = []

for i in range(2, 1000001):
    if seive[i]:
        primes.append(i)
    for j in range(i+i, 1000001, i):
        seive[j] = False

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    total = 0

    for p in primes:
        if p > N:  # N을 초과하기 전까지
            break
        if seive[N - p] and p <= N - p:     # N에서 p를 뺀 값도 prime이라면
            total += 1

    print(total)