dt = ((1, 0), (-1, 0), (0, 1), (0, -1))
def boom(x, y):
    m = balloons[x][y]
    sum_flo = 0

    sum_flo += balloons[x][y]
    for _x, _y in dt:
        for k in range(1, m+1):
            nx, ny = x + _x * k, y + _y * k

            if 0 <= nx < N and 0 <= ny < M:
               sum_flo += balloons[nx][ny]

    return sum_flo


T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())

    balloons = [list(map(int, input().split())) for _ in range(N)]

    max_boom = 0

    for i in range(N):
        for j in range(M):
            boom_v = boom(i, j)
            max_boom = max(boom_v, max_boom)

    print(f'#{tc} {max_boom}')