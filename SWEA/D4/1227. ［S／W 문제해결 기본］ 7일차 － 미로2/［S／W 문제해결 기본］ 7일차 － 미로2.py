dt = ((1, 0), (-1, 0), (0, 1), (0, -1))

def bfs(x, y, n):
    q = []                                      # 큐 생성
    visited = [[False] * 100 for _ in range(100)]   # visited 생성
    q.append([x, y])                            # 시작점 인큐
    visited[x][y] = True                        # 인큐 표시

    while q:                                    # 처리 안된 정점이 남아있으면 (큐에 값이 남아있으면)
        cx, cy = q.pop(0)                       # 현재 좌표

        # 기저 조건
        if cx == ex and cy == ey:                   # 목적지에 도달한 경우
            return 1

        for dx, dy in dt:
            nx = cx + dx                        # 델타값에 따라 위치 확인
            ny = cy + dy

            if 0 <= nx < n and 0 <= ny < n:   # 만약, 범위 내에 있으며,
                if maze[nx][ny] != 1 and not visited[nx][ny]:    # 통로이고, 그 중에서, 아직 방문하지 않은 곳이라면
                    q.append([nx, ny])      # 큐에 추가해주고
                    visited[nx][ny] = True  # 다음에 갈 곳의 visited에, 현재 나의 위치의 visited값 +1 을 할당

    return 0    # 큐가 전부 비워진다면 (검색에 실패했다면)


T = 10

for tc in range(1, T+1):
    tc_num = int(input())

    maze = [list(map(int, input().rstrip())) for _ in range(100)]    # 100x100 크기 미로 배열 입력받음

    # 시작점, 끝점 찾기
    for i in range(100):
        for j in range(100):
            if maze[i][j] == 2:
                sx, sy = i, j   # 시작 좌표
            elif maze[i][j] == 3:
                ex, ey = i, j   # 끝 좌표

    result = bfs(sx, sy, 100)
    print(f'#{tc}', result)
