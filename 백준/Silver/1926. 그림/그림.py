from collections import deque

# 델타값
dt = ((1, 0), (-1, 0), (0, 1), (0, -1))
def bfs(sx, sy):
    global paint_cnt, max_area

    # 큐 생성
    q = deque()
    # 카운트
    cnt_area = 1

    # 큐에 시작점 넣기
    q.append((sx, sy))
    # 시작점 방문처리
    visited[sx][sy] = True

    # 탐색 시작
    while q:
        # 현재 위치 꺼내기
        x, y = q.popleft()

        # 다음 좌표 확인
        for dx, dy in dt:
            nx, ny = x+dx, y+dy
            # 범위 내이며,
            if 0 <= nx < n and 0 <= ny < m:
                # 방문하지 않은 곳이며, 갈 수 있는 곳이라면,
                if not visited[nx][ny] and stage[nx][ny] == 1:
                    # 카운트
                    cnt_area += 1
                    # 큐에 넣기
                    q.append((nx, ny))
                    # 방문처리
                    visited[nx][ny] = True

    max_area = max(max_area, cnt_area)
    paint_cnt += 1


n, m = map(int, input().split())

stage = [list(map(int, input().split())) for _ in range(n)]

paint_cnt, max_area = 0, 0

# 방문 리스트 생성
visited = [[False] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        if not visited[i][j] and stage[i][j] == 1:
            bfs(i, j)

print(paint_cnt)
print(max_area)