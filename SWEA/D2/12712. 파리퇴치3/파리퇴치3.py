move_plus = [(1, 0), (0, 1), (0, -1), (-1, 0)]
def plus_sum(arr, i, j, n, m):
    sum_plus = 0
    for _i, _j in move_plus:
        for k in range(1, m):
            ni = i + _i * k
            nj = j + _j * k

            if 0 <= ni < n and 0 <= nj < n:
                sum_plus += arr[ni][nj]
    sum_plus += arr[i][j]
    return sum_plus


move_cross = [(1, 1), (-1, 1), (1, -1), (-1, -1)]
def cross_sum(arr, i, j, n, m):
    sum_cross = 0
    for _i, _j in move_cross:
        for k in range(1, m):
            ni = i + _i * k
            nj = j + _j * k

            if 0 <= ni < n and 0 <= nj < n:
                sum_cross += arr[ni][nj]
    sum_cross += arr[i][j]
    return sum_cross


T = int(input())

for tc in range(1, T + 1):
    # N x N 크기의 공간
    # M x M 크기의 파리채
    N, M = map(int, input().split())

    # 최대 파리수
    max_sum = 0

    # 공간에 존재하는 파리 마리 수
    area = [list(map(int, input().split())) for _ in range(N)]

    for i in range(N):
        for j in range(N):
            sum_pl = plus_sum(area, i, j, N, M)
            sum_cr = cross_sum(area, i, j, N, M)
            bigger = max(sum_pl, sum_cr)
            max_sum = max(bigger, max_sum)

    print(f'#{tc} {max_sum}')