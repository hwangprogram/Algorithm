# 입력
# 테스트 케이스 T
T = int(input())

for tc in range(1, T + 1):
    # N 크기의 달팽이
    N = int(input())

    # 로직
    # 델타 값
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]

    # 칸에 채워넣을 숫자 cnt
    cnt = 1

    # 현재 나의 방향값은?
    vec = 0

    # 나는 지금 어디인가?
    i, j = 0, 0

    # 어디에 값을 채울것인가?
    arr = [[0] * N for _ in range(N)]

    # 언제까지 진행해야 하는가?
    while cnt != N * N + 1:

        # 다음에 오는값의 유효성 검사
        ni, nj = i + di[vec], j + dj[vec]

        # 다음에 올 값이 인덱스 범위 내에 있지 않다면?, 다음에 올 칸이 이미 차있으면?
        # 방향을 돌린다. 어디로? 오 아래 왼 위
        if ni < 0 or ni >= N or nj < 0 or nj >= N or arr[ni][nj] != 0:
            vec = (vec + 1) % 4

        # 그렇지 않다면?
        arr[i][j] = cnt
        cnt += 1
        i += di[vec]
        j += dj[vec]

    # 출력
    print(f'#{tc}')
    for i in range(N):
        print(*arr[i])