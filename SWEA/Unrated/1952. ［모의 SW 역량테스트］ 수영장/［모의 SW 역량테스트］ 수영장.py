# 깊이 우선 탐색: 1일권, 1달권, 3달권, 1년권
def dfs(idx, cost):
    global min_cost

    # 가지치기 : min_cost 이상이면 return
    if cost >= min_cost:
        return

    # 기저조건 : 12월 초과되면 return
    if idx == 13:
        # 정답조건 : 가장 작은 cost 값을 return
        min_cost = min(min_cost, cost)
        return

    # 재귀조건 : 1일, 1달, 3달, 1년(12달) 차례로 탐색 시작
    # 1일
    dfs(idx+1, cost+(fee[0]*plan[idx-1]))

    # 1달
    dfs(idx+1, cost+fee[1])

    # 3달
    # 인덱스 초과 방지 10월 전까지
    if idx <= 10:
        dfs(idx+3, cost+fee[2])

    # 1년
    # 인덱스 초과 방지 1월만
    if idx == 1:
        dfs(idx+12, cost+fee[3])


T = int(input())

for tc in range(1, T+1):
    fee = list(map(int, input().split()))
    plan = list(map(int, input().split()))

    min_cost = 3000*12

    dfs(1, 0)
    print(f"#{tc} {min_cost}")