T = int(input())

for tc in range(1, T+1):
    N = int(input())
    dp = [0] * (N+1)

    if N >= 1:
        dp[1] = 1
    if N >= 2:
        dp[2] = 2
    if N >= 3:
        dp[3] = 4
    if N > 3:
        for n in range(4, N+1):
            dp[n] = dp[n-1] + dp[n-2] + dp[n-3]

    print(dp[N])