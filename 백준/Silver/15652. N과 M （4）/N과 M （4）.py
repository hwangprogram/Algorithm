import sys
input = sys.stdin.readline

path = []
def recursion(n, m):
    # 기저조건: M개를 골랐다면 return
    if len(path) == M:
        print(*path)
        return

    for i in range(m, n+1):
        path.append(i)
        recursion(n, i)
        path.pop()


N, M = map(int, input().split())

recursion(N, 1)
