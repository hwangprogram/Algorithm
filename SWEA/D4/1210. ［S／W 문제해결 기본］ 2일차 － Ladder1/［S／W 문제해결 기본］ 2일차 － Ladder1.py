T = 10

for tc in range(1, T + 1):
    # 입력
    # 테스트 케이스 숫자
    T_num = int(input())

    # 사다리 ladder
    ladder = [list(map(int, input().split())) for _ in range(100)]

    # 로직
    # 나는 어디에 있는가?
    i, j = 0, 0

    # 어디로 가야하는가?
    di = [1, 0, 0]
    dj = [0, 1, -1]

    # 나의 현재 방향은?
    vec = 0

    # 정답
    ans = 0

    # 어디서 출발하는가?
    for i in range(100):
        if ladder[0][i] == 1:
            cx, cy = 0, i

            # 어디로 가는가?
            # 다른 값 찾기 전까지 같은 방향으로 계속 가야함
            while cx != 99:

                vec = 0
                cx += di[vec]
                cy += dj[vec]

                # 오른쪽
                if cy < 99 and ladder[cx][cy + 1] == 1:
                    while cy < 99 and ladder[cx][cy + 1] == 1:
                        vec = 1
                        cx += di[vec]
                        cy += dj[vec]
                # 왼쪽
                elif cy > 0 and ladder[cx][cy - 1] == 1:
                    while cy > 0 and ladder[cx][cy - 1] == 1:
                        vec = 2
                        cx += di[vec]
                        cy += dj[vec]


                if ladder[cx][cy] == 2:
                    ans = i
                    break

    print(f'#{tc} {ans}')