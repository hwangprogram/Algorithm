dt_plus = ((1, 0), (-1, 0), (0, 1), (0, -1))        # +모양 스프레이
def kill_plus(x, y, m):
    sum_fly = 0

    sum_fly += flies[x][y]
    for _x, _y in dt_plus:
        for k in range(1, m):
            nx, ny = x + _x * k, y + _y * k

            if 0 <= nx < N and 0 <= ny < N:
               sum_fly += flies[nx][ny]

    return sum_fly

dt_cross = ((1, 1), (1, -1), (-1, 1), (-1, -1))     # x모양 스프레이
def kill_cross(x, y, m):
    sum_fly = 0

    sum_fly += flies[x][y]
    for _x, _y in dt_cross:
        for k in range(1, m):
            nx, ny = x + _x * k, y + _y * k

            if 0 <= nx < N and 0 <= ny < N:
                sum_fly += flies[nx][ny]

    return sum_fly


T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())

    flies = [list(map(int, input().split())) for _ in range(N)]

    max_fin = 0
    for i in range(N):
        for j in range(N):
            plus = kill_plus(i, j, M)
            cross = kill_cross(i, j, M)

            max_both = max(plus, cross)
            max_fin = max(max_fin, max_both)

    print(f'#{tc} {max_fin}')