'''
백준 15649 N과 M

전략:
used배열을 사용해서 쓴값을 다시 고르지 못하도록
재귀함수를 생성한다.
'''

path = []
def recursion(n, m):
    # 기저조건: M개를 골랐다면 return
    if len(path) == M:
        print(*path)
        return

    for i in range(1, n+1):
        path.append(i)
        recursion(n, i+1)
        path.pop()


N, M = map(int, input().split())

recursion(N, 1)
