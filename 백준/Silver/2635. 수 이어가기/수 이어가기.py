N = int(input())

dp = [0] * 2     # 값 쌓아줄 리스트
mx_cnt = 0      # 맥스 카운트
result = []     # 결과값 리스트

for i in range(1, N+1):
    dp[0] = N  # 첫 번째 값
    dp[1] = i     # 두 번째 값
    cnt = 1     # 카운트

    i = 0
    while dp[-1] >= 0:    # 리스트의 마지막 수가 0보다 클 때까지
        dp.append(dp[i] - dp[i+1])
        cnt += 1
        i += 1
    dp.pop()

    if cnt > mx_cnt:
        result = dp[:]  # 그 리스트 복사
        mx_cnt = cnt    # 최대 카운트 계산

    dp = [0] * 2     # 배열 초기화

print(mx_cnt)
print(*result)