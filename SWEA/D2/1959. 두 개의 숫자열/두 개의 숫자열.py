T = int(input())

for tc in range(1, T + 1):
    # A_lst의 길이 N, B_lst의 길이 M
    N, M = map(int, input().split())

    # 숫자열 A_lst, B_lst
    A_lst = list(map(int, input().split()))
    B_lst = list(map(int, input().split()))

    # 곱의 합 mul_sum
    mul_sum = 0
    max_v = 0

    # 짧은 쪽이 긴쪽을 순회
    if N <= M:
        for i in range(M - N + 1):
            for j in range(N):
                mul_sum += A_lst[j] * B_lst[i + j]
            max_v = max(mul_sum, max_v)
            mul_sum = 0
    else:
        for i in range(N - M + 1):
            for j in range(M):
                mul_sum += A_lst[i + j] * B_lst[j]
            max_v = max(mul_sum, max_v)
            mul_sum = 0

    print(f'#{tc} {max_v}')
