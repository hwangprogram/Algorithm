from collections import deque

# bfs
def bfs(n):
    global ans

    # 큐 생성
    q = deque()
    # 카운트
    cnt = 0
    # 시작점, 카운트 추가
    q.append((n, cnt))

    # 방문 리스트
    visited = [False] * 101

    # 방문처리
    visited[n] = True

    # 최신화 할 카운트
    mx_cnt = 0

    # 탐색 시작
    while q:
        node, count = q.popleft()

        # 깊어질때 마다 초기화
        if mx_cnt < count:
            ans = 0
            mx_cnt = count

        # 최대 깊이 노드 중 최대값
        ans = max(node, ans)

        # 다음 노드 선택
        for nxt in adjl[node]:
            # 방문하지 않은 곳이라면 방문 처리 및 큐에 추가
            if not visited[nxt]:
                visited[nxt] = True
                q.append((nxt, count+1))


T = 10

for tc in range(1, T+1):
    # 간선길이 E, 시작점 S
    E, S = map(int, input().split())

    # 간선정보 lst
    lst = list(map(int, input().split()))

    # 인접 리스트 adjl
    adjl = [[] for _ in range(101)]
    for e in range(0, E, 2):
        now, to = lst[e], lst[e+1]

        adjl[now].append(to)

    # 최댓값 노드
    ans = 0

    bfs(S)
    print(f'#{tc} {ans}')