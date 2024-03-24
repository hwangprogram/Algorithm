def find_set(x):
    # 기저조건: 내가 부모라면 return
    if x == parents[x]:
        return x

    # 재귀조건: 부모를 찾아 탐색
    return find_set(parents[x])

def union(x, y):
    root_x = find_set(x)
    root_y = find_set(y)

    # 작은 부모로 합치기
    if root_x < root_y:
        parents[root_y] = parents[root_x]
    else:
        parents[root_x] = parents[root_y]


T = int(input())

for tc in range(1, T+1):
    N = int(input())

    point = [[] for _ in range(N)]
    x_lst = list(map(int, input().split()))
    y_lst = list(map(int, input().split()))

    # 환경 세율 E
    E = float(input())

    # 시작정점, 도착정점, 가중치로 이루어진 리스트들 생성
    edges = []
    # 부모 형성
    parents = list(range(N))
    for i in range(N):
        for j in range(i+1, N):
            # 각 시작 -> 도착 정점으로 가는 가중치 append
            # 가중치? (환경 세율 E) x (좌표 에서 좌표로 가는 거리 L) ^ 2
            distance = (x_lst[i] - x_lst[j]) ** 2 + (y_lst[i] - y_lst[j]) ** 2
            weight = E * distance

            edges.append([i, j, weight])

    # edges를 가중치 기준으로 오름차순 정렬
    edges.sort(key=lambda x: x[2])

    # MST 완성: 간선의 갯수가 V-1개가 될 때
    # 최종 가중치
    sum_weight = 0
    # 간선의 갯수 세어줄 변수
    cnt = 0

    # 간선들 모두 확인
    for s, e, w in edges:
        # 이미 같은 집합에 속해 있다면 -> 사이클이 형성되었다면
        if find_set(s) == find_set(e):
            continue

        # 아니라면
        # 카운트
        cnt += 1
        # 합치기
        union(s, e)
        # 가중치 합
        sum_weight += w

        # MST 완성 -> 간선의 갯수가 N-1개
        if cnt == N-1:
            break

    print(f"#{tc} {round(sum_weight)}")
