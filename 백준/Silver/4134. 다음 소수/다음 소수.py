'''
# 4134 다음 소수

문제 요약
n보다 크거나 같은 소수 중 가장 작은 소수를 찾는 프로그램을 작성하라
'''
import math

def is_prime(n):
    if n == 0 or n == 1:
        return False

    if n <= 3:
        return True

    if n % 2 == 0 or n % 3 == 0:
        return False

    j = 5
    while j * j <= n:
        if n % j == 0 or n % (j + 2) == 0:
            return False
        j += 6
    return True


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    cnt = 0

    while True:
        if is_prime(N):
            print(N)
            break
        N += 1