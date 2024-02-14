T = int(input())

for tc in range(1, T+1):
    # N줄에 걸쳐 현재 방, 가야할 방 번호
    N = int(input().rstrip())
    # 카운트 배열
    cnt_lst = [0] * 201
    for n in range(N):
        n1, n2 = map(int, input().split())
        n1 = (n1 + 1) // 2
        n2 = (n2 + 1) // 2

        if n1 <= n2:
            for i in range(n1, n2 + 1):
                cnt_lst[i] += 1
        else:
            for i in range(n2, n1 + 1):
                cnt_lst[i] += 1
    ans = max(cnt_lst)
    print(f'#{tc} {ans}')
