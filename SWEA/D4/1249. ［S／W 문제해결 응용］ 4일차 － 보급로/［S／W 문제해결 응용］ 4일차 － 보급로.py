from heapq import heappush, heappop

dt = ((1, 0), (-1, 0), (0, 1), (0, -1))
def dijkstra(sx, sy):
    pq = []

    # 시작 정점의 weight, 좌표를 저장
    heappush(pq, (0, sx, sy))
    # 시작 좌표 초기화
    dist[sx][sy] = 0

    while pq:
        # 최단 거리 좌표에 대한 정보
        weight, x, y = heappop(pq)

        # 현재 좌표가 더 짧은 거리로 온 적이 있다면 pass
        if dist[x][y] < weight:
            continue

        # 인접한 좌표들 확인
        for dx, dy in dt:
            nx, ny = x + dx, y + dy

            # 범위 안에 있다면
            if 0 <= nx < N and 0 <= ny < N:
                nw = info[nx][ny]
                # 새로 갱신해 줄 거리값
                new_weight = weight + nw
                # 새로운 거리값이 짧을 때만 갱신
                if new_weight < dist[nx][ny]:
                    dist[nx][ny] = new_weight
                    # 다음 좌표 넣어주기
                    heappush(pq, (new_weight, nx, ny))


T = int(input())

for tc in range(1, T+1):
    N = int(input())

    # 복구해야하는 땅 정보
    info = [list(map(int, input())) for _ in range(N)]

    # 누적 거리 저장할 리스트
    dist = [[float('inf')] * N for _ in range(N)]

    dijkstra(0, 0)
    print(f"#{tc} {dist[N-1][N-1]}")