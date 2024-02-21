# 이진탐색 (binary search) 사용
def binary_search(n):
    start = 0
    end = 10 ** 6       # 어느 범위 내에 있는지
    while start <= end:
        middle = (start + end) // 2
        if middle ** 3 == N:
            return middle
        elif middle ** 3 > N:
            end = middle - 1
        else:
            start = middle + 1
    return -1


T = int(input())

for tc in range(1, T+1):
    N = int(input())

    ans = binary_search(N)
    print(f'#{tc} {ans}')