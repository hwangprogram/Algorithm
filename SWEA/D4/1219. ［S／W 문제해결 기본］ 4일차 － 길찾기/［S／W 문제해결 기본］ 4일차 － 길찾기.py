def dfs(i):     # 시작 i, 마지막 v
    visited[i] = 1  # 방문표시
    # i에 인접하고 방문안한 w가 있으면
    for w in adjl[i]:
        if visited[w] == 0:
            dfs(w)

T = 10

for tc in range(1, T+1):
    test_case, E = map(int, input().split())

    n_lst = list(map(int, input().split()))

    visited = [0] * 100      # 방문 여부 확인

    # 인접리스트
    adjl = [[] for _ in range(100)]  # adjl[i] 행에 i에 인접인 정점번호

    for i in range(E):
        n1, n2 = n_lst[2*i], n_lst[2*i+1]
        adjl[n1].append(n2)

    # print(adjl)
    # 끝까지 도착했는지 확인하는 변수
    ans = 0

    dfs(0)
    if visited[99] == 1:
        ans = 1

    print(f'#{tc} {ans}')
