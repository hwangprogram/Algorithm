def inorder(i):
    if i == 0:
        return
    inorder(left[i])
    print(node[i], end='')
    inorder(right[i])


T = 10

for tc in range(1, T+1):
    N = int(input())

    par = [0] * (N + 1)
    left = [0] * (N + 1)
    right = [0] * (N + 1)
    node = [0] * (N + 1)

    for _ in range(N):
        pnlr = list(input().split())


        if len(pnlr) == 4:      # 왼, 오 자식 둘다 있다면
            left[int(pnlr[0])] = int(pnlr[2])       # 왼쪽 자식
            right[int(pnlr[0])] = int(pnlr[3])      # 오른쪽 자식
            par[int(pnlr[2])] = int(pnlr[0])        # 부모
            par[int(pnlr[3])] = int(pnlr[0])        # 값
            node[int(pnlr[0])] = pnlr[1]
        elif len(pnlr) == 3:    # 왼쪽 자식만 있다면
            left[int(pnlr[0])] = int(pnlr[2])       # 왼쪽 자식
            par[int(pnlr[2])] = int(pnlr[0])        # 부모
            node[int(pnlr[0])] = pnlr[1]            # 값
        else:   # 값만 있다면
            node[int(pnlr[0])] = pnlr[1]            # 값

    print(f'#{tc}', end=' ')
    inorder(1)
    print()