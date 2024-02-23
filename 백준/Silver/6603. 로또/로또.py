def make_subset(cnt, idx):
    # 기저조건
    if cnt == 6:
        print(*result)
        return

    for i in range(idx, K):
        result.append(S[i])
        make_subset(cnt+1, i+1)
        result.pop()


while True:
    S = list(map(int, input().split()))

    if S[0] == 0:
        break

    result = []
    K = S.pop(0)

    make_subset(0, 0)
    print()