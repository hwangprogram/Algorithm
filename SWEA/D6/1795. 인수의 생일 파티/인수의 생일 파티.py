from heapq import heappop, heappush

T = int(input())

for tc in range(1, T+1):
    # N개의 정점, M개의 간선, X노드에서 시작
    N, M, X = map(int, input().split())
    N += 1

    # 인접 리스트
    adjl = [[] for _ in range(N)]
    for _ in range(M):
        # x -> y로 가는데 c의 가중치 소요
        x, y, c = map(int, input().split())
        # y 로 가는 간선의 가중치가 c
        adjl[x].append((y, c))

    def dijkstra(graph, start):
        # 시작 정점에서 각 정점까지의 최소 거리를 계산하는 배열 dist
        dist = [float('inf')] * N

        # 시작 정점 방문체크, dist 거리 초기화
        dist[start] = 0

        # 시작 정점부터 진행
        mheap = [(0, start)]

        while mheap:
            cost, node = heappop(mheap)

            # 이미 계산되어 있는 dist보다 더 거리가 긴 노드라면 패스
            if cost > dist[node]:
                continue

            # 인접 노드와 거리를 순차적으로 뽑아서 큐에서 넣어주고 dist 갱신
            for nxt, w in graph[node]:
                # 새로 갱신될 거리값
                new_dist = dist[node] + w
                if new_dist < dist[nxt]:
                    dist[nxt] = new_dist
                    heappush(mheap, (new_dist, nxt))
        return dist


    # X번 노드로부터 모든 노드까지 경로 비용 출력
    dist = dijkstra(adjl, X)[1:]
    # 다른 노드들로부터 X번 노드까지 경로 비용 저장할 리스트
    dist_toX = []
    for n in range(1, N):
        dist_toX.append(dijkstra(adjl, n)[X])
    res = list(map(lambda x1, x2: x1+x2, dist, dist_toX))
    print(f"#{tc} {max(res)}")