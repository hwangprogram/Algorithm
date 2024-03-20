def dfs(row, per):
    global max_per

    # 가지치기: max_per보다 작으면 종료
    if per <= max_per:
        return

    # 기저조건: row가 마지막까지 가면 종료
    if row == N:
        # 정답조건: 최대 성공확률 반환
        max_per = max(per, max_per)
        return

    for col in range(N):
        # 방문한 열이라면 pass
        if visited[col]:
            continue

        # 방문처리
        visited[col] = True
        # 재귀
        dfs(row+1, per * (works[row][col]/100))
        # 초기화
        visited[col] = False


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    works = [list(map(int, input().split())) for _ in range(N)]

    # 열 visited배열
    visited = [False] * N

    max_per = 0
    dfs(0, 1)
    print(f"#{tc} {max_per*100:.6f}")