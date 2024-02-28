path = []
def sub_set(n):
    # 기저조건
    if n == N:
        print(*path)
        return

    for i in range(N):
        path.append(N_lst[i])
        sub_set(n+1)
        path.pop()


T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    N_lst = list(map(int, input().split()))

    cnt = 0
    set_lst = []
    for i in range(1<<N):
        sum_v = 0
        for j in range(N):
            if i & (1<<j):
                sum_v += N_lst[j]

        if sum_v == K:
            cnt += 1

    print(f'#{tc} {cnt}')