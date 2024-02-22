dt = ((1, 0), (-1, 0), (0, 1), (0, -1))

def find_route(x, y, dist, K):
    global route

    if dist > route:
        route = dist        # route 에 최댓값 저장

    visited[x][y] = 1       # 방문표시

    for _x, _y in dt:
        nx, ny = x + _x, y + _y     # 4방향 탐색

        if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
            if map_info[x][y] > map_info[nx][ny]:     # 방문한적 없고, 현재 높이보다 낮으면
                find_route(nx, ny, dist+1, K)
            elif K and K > map_info[nx][ny] - map_info[x][y]:    # 방문한적 없고, 높이의 차가 K보다 적다면
                tmp = map_info[nx][ny]
                map_info[nx][ny] = map_info[x][y] - 1            # 결국 현재 좌표에서 1을 뺀값까지만 빼면 되므로
                find_route(nx, ny, dist+1, 0)
                map_info[nx][ny] = tmp

    visited[x][y] = 0       # 방문여부 초기화


T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())      # NxN 크기의 지도, 팔 수 있는 땅의 깊이 K

    map_info = [list(map(int, input().split())) for _ in range(N)]  # 지도 정보

    # 봉우리 찾기
    max_h = 0

    for i in range(N):
        for j in range(N):
            if map_info[i][j] > max_h:
                max_h = map_info[i][j]

    # 봉우리에서 탐색 시작
    route = 0  # 최고 길이 등산로 길이
    visited = [[0 for _ in range(N)] for _ in range(N)]  # 방문여부 배열

    for i in range(N):
        for j in range(N):
            if map_info[i][j] == max_h:
                find_route(i, j, 1, K)

    print(f'#{tc} {route}')