# 델타
dx = [1, 0, -1, 0, 1, 1, -1, -1]
dy = [0, 1, 0, -1, 1, -1, 1, -1]

T = int(input())

for tc in range(1, T+1):
    # N 바둑판 한변의 길이
    # M 개의 수
    N, M = map(int, input().split())

    oselo = [[0] * N for _ in range(N)]             # 바둑판

    oselo[N // 2 - 1][N // 2 - 1] = oselo[N // 2][N // 2] = 2   # 백
    oselo[N // 2][N // 2 - 1] = oselo[N // 2 - 1][N // 2] = 1   # 흑

    for i in range(M):
        x, y, color = map(int, input().split())     # 바둑알을 놓을 x,y 좌포, 돌의 색
        x -= 1
        y -= 1
        oselo[x][y] = color

        # 상하좌우 또는 대각선에서 다른 색깔 돌을 발견했을 때, 그쪽으로 계속 파고들어가서 같은 색을 만날 때 까지 반복한다.
        for j in range(8):
            stack = []
            for k in range(1, N):
                nx, ny = x + dx[j] * k, y + dy[j] * k
                if 0 <= nx < N and 0 <= ny < N:
                    stack.append([nx, ny])
                    if oselo[nx][ny] == color:
                        for q, p in stack:
                            oselo[q][p] = color
                        break
                    elif oselo[nx][ny] == 0:
                        break

    black = white = 0

    for j in oselo:
        black += j.count(1)
        white += j.count(2)

    print(f'#{tc}', black, white)