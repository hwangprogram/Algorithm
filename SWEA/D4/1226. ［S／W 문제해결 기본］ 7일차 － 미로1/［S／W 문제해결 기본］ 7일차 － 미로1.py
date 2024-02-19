dt = ((1, 0), (-1, 0), (0, 1), (0, -1))


def bfs(x, y, n):           # 이진 탐색
    q = []                  # 큐 생성
    visited = [[False] * n for _ in range(n)]   # visited 생성
    q.append([x, y])        # 시작점 인큐
    visited[x][y] = True    # 방문 표시

    while q:                # 큐에 값이 빌때 까지 진행 (모든 정점 처리)
        cx, cy = q.pop(0)   # 현재 좌표

        # 기저조건
        if cx == ex and cy == ey:
            return 1

        for _x, _y in dt:
            nx = cx + _x
            ny = cy + _y

            if 0 <= nx < n and 0 <= ny < n:     # 범위 내라면
                if maze[nx][ny] != 1 and not visited[nx][ny]:  # 통로이고, 방문한 적 없다면,
                    q.append([nx, ny])    # q에 추가해주고
                    visited[nx][ny] = True  # 방문처리
    return 0    # 큐가 다 비워질 때 까지 값이 나오지 않았다면 길 x


T = 10

for tc in range(1, T + 1):
    test_case = int(input())

    maze = [list(map(int, input())) for _ in range(16)]

    for i in range(16):
        for j in range(16):
            if maze[i][j] == 2:
                sx, sy = i, j
            elif maze[i][j] == 3:
                ex, ey = i, j

    print(f'#{test_case} {bfs(sx, sy, 16)}')