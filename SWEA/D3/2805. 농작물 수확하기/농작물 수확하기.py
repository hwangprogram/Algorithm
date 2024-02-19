T = int(input())

for tc in range(1, T + 1):
    N = int(input())    # 농장크기
    farm = [list(map(int, input())) for _ in range(N)]      # 농장

    sum_num = 0

    n = N // 2      # 인덱스의 반 값
    idx_lst = []        # 더해줄 인덱스들의 값을 넣어줄 배열
    for i in range(n + 1):
        idx_lst.append(list(range(n - i, n + i + 1)))
    for i in range(n - 1, -1, -1):
        idx_lst.append(list(range(n - i, n + i + 1)))

    for i in range(N):
        for idx in idx_lst[i]:
            sum_num += farm[i][idx]

    print(f'#{tc} {sum_num}')