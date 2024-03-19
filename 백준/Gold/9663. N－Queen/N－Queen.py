import sys
input = sys.stdin.readline

# N-퀸 문제

# 내가 해당 (row, col)에 퀸을 배치할 수 있는지 check
# 대각선에 대해서 서로 영역이 겹치지 않는지만 간단하게 체크
def check(row, col):
    # 이전까지 놓아져 있는 퀸이 (x, y)
    for x in range(row):    # [0, row]
        y = board[x]
    # 내가 놓으려고 하는 (row, col)의 위치와 대각선 영역이 서로 겹치는가
        if abs(x - row) == abs(y - col):
            return False    # 놓을 수 없음

    # 해당 위치에는 퀸을 배치할 수 있다.
    return True

# 완전탐색(DFS)
def dfs(depth):
    global count
    # 기저조건(종료조건): depth가 퀸의 갯수 만큼 카운트가 되었을 때
    # => 퀸이 N개 놓여져 있을 때 중단하겠다.
    if depth == N:
        count += 1
        return

        # 재귀적으로 말을 배치
    # 반복문을 통해서 1부터 N번까지의 모든 위치에 말을 놓아보도록 시도
    for col in range(N):
        # 해당 행에 퀸을 배치 (depth, col)
        if not visited[col] and check(depth, col):
            # TODO: 해당 위치에 배치를 할 수 있는지 체크
            board[depth] = col
            # visited 배열을 통해 동일한 행(col)에 대해 다른 퀸이 들어가지 않도록 체크
            visited[col] = True  # 결정
            dfs(depth + 1)
            visited[col] = False  # 복구


# N-퀸을 놓을 수 있는 횟수를 카운트하여 출력
N = int(input())  # N퀸의 N을 입력으로 받음
# 카운트 변수 (글로벌)
count = 0
visited = [False] * N
# 배치할 말의 위치 board
board = [-1] * N
dfs(0)
print(count)