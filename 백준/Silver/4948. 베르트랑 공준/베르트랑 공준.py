'''
# 4948 베르트랑 공준

문제 요약
n이 주어졌을 때, n보다 크고, 2n보다 작거나 같은 소수의 개수를 구하라
'''

#
def prime(n):
    seive = [True] * (2 * n)

    # n의 최대 약수는 n의 제곱근 이하이다.
    m = int((2 * n) ** 0.5)
    for i in range(2, m + 1):
        for j in range(2 * i, 2 * n, i):
            seive[j] = False

    return [i for i in range(n + 1, 2 * n) if seive[i]]


while True:

    N = int(input())

    if N == 0:
        break

    result = prime(N)
    if N == 1:
        result.append(2)
    print(len(result))