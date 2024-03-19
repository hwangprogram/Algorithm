dt = ((1, 0), (-1, 0), (0, 1), (0, -1))
def dfs(i, j, path):
    # 기저조건 : path의 길이가 7이 되면 종료
    if len(path) == 7:
        path_set.add(path)
        return

    # 재귀조건 : 방문 여부 상관 x 동서남북으로 이동
    for di, dj in dt:
        ni = i + di
        nj = j + dj

        if 0 <= ni < 4 and 0 <= nj < 4:
            dfs(ni, nj, path+str(grid[ni][nj]))


T = int(input())

for tc in range(1, T+1):
    # 격자판
    grid = [list(map(int, input().split())) for _ in range(4)]
    path_set = set()
    for i in range(4):
        for j in range(4):
            dfs(i, j, str(grid[i][j]))

    print(f"#{tc} {len(path_set)}")