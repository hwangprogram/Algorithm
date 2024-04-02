def dfs(idx, p, m, c, d, val):
    global mx_val, mn_val

    # 기저조건: path가 N-1길이가 되면 종료
    if idx == N:
        # 정답처리: 최대, 최소값 확인
        if val > mx_val:
            mx_val = val
        if val < mn_val:
            mn_val = val
        return

    # 연산(재귀)
    # plus값 남았다면
    if p:
        dfs(idx+1, p-1, m, c, d, val+nums[idx])
    if m:
        dfs(idx+1, p, m-1, c, d, val-nums[idx])
    if c:
        dfs(idx+1, p, m, c-1, d, val*nums[idx])
    if d:
        dfs(idx+1, p, m, c, d-1, int(val/nums[idx]))


T = int(input())

for tc in range(1, T+1):
    # 숫자 개수 N
    N = int(input())
    # + - * /
    plus, minus, comp, devide = map(int, input().split())
    # 숫자들
    nums = list(map(int, input().split()))

    # 최대값, 최소값
    mn_val, mx_val = float('inf'), -float('inf')

    dfs(1, plus, minus, comp, devide, nums[0])
    ans = mx_val - mn_val
    print(f'#{tc} {ans}')