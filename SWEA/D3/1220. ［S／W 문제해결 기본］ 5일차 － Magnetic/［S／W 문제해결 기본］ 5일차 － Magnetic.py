T = 10

for tc in range(1, T+1):
    N = int(input())
    magnetic = [list(map(int, input().split())) for _ in range(100)]

    magnetic = [list(tp) for tp in zip(*magnetic)]

    total = 0
    for i in range(N):
        flag = 0
        for j in range(N):
            if magnetic[i][j] == 1:         # N극을 만나면 flag를 1로 변경
                flag = 1
            elif magnetic[i][j] == 2:       # S극을 만났고, 현재 플래그가 1이라면 카운트해주고 플래그 초기화
                if flag:
                    total += 1
                    flag = 0

    print(f'#{tc} {total}')