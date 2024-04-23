from collections import deque

dt = ((1, 0), (-1, 0), (0, 1), (0, -1))
def bfs():
    global max_cnt

    # 탐색
    while q:
        # 현재 값 꺼내서 확인
        x, y, cnt = q.popleft()

        max_cnt = max(cnt, max_cnt)

        # 다음 좌표 탐색
        for dx, dy in dt:
            nx, ny = x+dx, y+dy

            # 범위 내인지 확인
            if 0 <= nx < N and 0 <= ny < M:
                # 방문 가능한지 확인
                if tomatos[nx][ny] == 0:
                    # 방문처리
                    tomatos[nx][ny] = 1
                    # 큐에 넣기
                    q.append((nx, ny, cnt+1))


M, N = map(int, input().split())
tomatos = [list(map(int, input().split())) for _ in range(N)]

# 큐 생성
q = deque()
# 정답
max_cnt = 0

for i in range(N):
    for j in range(M):
        # 익은 토마토라면
        if tomatos[i][j] == 1:
            # 좌표, 카운트 큐에 넣기
            q.append((i, j, 0))

# 시작점들을 가진 큐를 가지고 탐색 시작
bfs()

# 0 있는지 확인 (있다면 전부 탐색 x)
for i in range(N):
    for j in range(M):
        if tomatos[i][j] == 0:
            max_cnt = -1
            break

print(max_cnt)