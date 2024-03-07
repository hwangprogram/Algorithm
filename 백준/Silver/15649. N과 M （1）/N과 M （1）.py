'''
백준 15649 N과 M

전략:
used배열을 사용해서 쓴값을 다시 고르지 못하도록
재귀함수를 생성한다.
'''

path = []
def recursion(n, m):
    # 기저조건: M개를 골랐다면 return
    if m == M:
        print(*path)
        return

    for i in range(1, n+1):
        # 방문하지 않았다면
        if not used[i]:
            # 방문처리
            used[i] = True
            path.append(i)
            recursion(n, m+1)
            # 초기화
            path.pop()
            used[i] = False


N, M = map(int, input().split())

# used 배열
used = [False] * (N+1)

recursion(N, 0)