'''
SWEA 세제곱근을 찾아라

문제 요약
양의 정수 N에 대해 N = x^3이 되는 양의 정수 x를 구하라
'''

def binary_search(n):
    start = 0
    end = n
    while start <= end:
        middle = (start + end) // 2

        if middle ** 3 == n:
            return middle
        elif middle ** 3 < n:
            start = middle + 1
        elif middle ** 3 > n:
            end = middle - 1

    return -1


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    res = binary_search(N)

    print(f'#{tc} {res}')