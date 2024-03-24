'''
SWEA 창용마을 무리의 개수

문제요약:
마을에 서로 알고있는 사람들의 무리 개수가 얼마나 되는지 세어라

문제의도:
find-union set을 통해 알고 있는 사람들을 union 해준다.
'''

def find(x):
    # 기저조건: 대표자(부모)가 나 자신이라면 return
    if x == parent[x]:
        return x

    # 재귀조건: 부모를 찾아가기
    parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    # 각 요소의 부모 찾기
    root_x = find(x)
    root_y = find(y)

    # 제약조건: 더 작은것을 부모로 만들 것
    if root_x < root_y:
        parent[root_y] = root_x
    else:
        parent[root_x] = root_y


T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    N += 1

    # init: 나 자신을 부모로 갖는 트리 갖기
    parent = list(range(N))
    for _ in range(M):
        n1, n2 = map(int, input().split())

        # union: n1과 n2에 속한 두 그룹을 하나로 합쳐라
        union(n1, n2)

    ans = set()
    for i in range(1, N):
        ans.add(find(i))

    print(f"#{tc} {len(ans)}")