path = []
def recursion(n, m):
    # 기저조건: M개를 골랐다면 return
    if len(path) == M:
        print(*path)
        return

    for i in range(m, n+1):
        # 방문하지 않았다면
        if i not in path:
            # 방문처리
            path.append(i)
            recursion(n, i+1)
            # 초기화
            path.pop()


N, M = map(int, input().split())

recursion(N, 1)
