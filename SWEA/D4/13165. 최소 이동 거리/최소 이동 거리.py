from heapq import heappop, heappush
def dijkstra(graph, start):
    # 시작 정점에서 각 정점까지의 최소 거리를 계산하는 배열
    dist = [float('inf')] * N

    # 시작 정점 방문체크, dist거리 0으로 초기화
    dist[start] = 0

    # 시작 정점으로부터 진행
    mheap = [(0, start)]

    while mheap:
        cost, node = heappop(mheap)

        # 이미 계산된 노드보다 더 거리가 긴 노드라면 패스
        if cost > dist[node]:
            continue

        # 인접해있는 노드와 거리를 순차적으로 뽑아 큐에 넣어주기
        for nxt, w in graph[node]:
            # 새로 갱신될 거리값
            new_dist = dist[node] + w
            # 새로 갱신된 거리값이 현재 값보다 작을 때만 갱신
            if new_dist < dist[nxt]:
                dist[nxt] = new_dist
                heappush(mheap, (new_dist, nxt))

    return dist


T = int(input())

for tc in range(1, T+1):
    N, E = map(int, input().split())
    N += 1

    # 인접 리스트 adjl
    adjl = [[] * N for _ in range(N)]
    for _ in range(E):
        s, e, w = map(int, input().split())

        # 시작점의 인접 노드에 도착점, 가중치 요소를 가진 튜플 추가
        adjl[s].append((e, w))

    dist = dijkstra(adjl, 0)

    print(f"#{tc} {dist[-1]}")