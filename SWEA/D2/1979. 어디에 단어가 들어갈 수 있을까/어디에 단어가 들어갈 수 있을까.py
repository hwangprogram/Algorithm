T = int(input())

for tc in range(1, T + 1):
    # 입력
    # N x N 크기의 단어 퍼즐
    # 길이 K를 갖는 단어
    N, K = map(int, input().split())
    # 퍼즐의 모양 pz
    pz = [list(map(int, input().split())) for _ in range(N)]

    # 로직
    # 가로, 세로를 순회하며, 1 값을 찾음
    # 1값을 카운트하고, K값과 동일한 경우를 카운트하는 변수 cnt
    cnt = 0
    ct = 0

    # 가로 칸 수 세기
    for i in range(N):
        for j in range(N):
            # 좌표값의 값을 확인 (1인지 아닌지)
            if pz[i][j] == 1:
                # 만약 1이라면 ct + 1
                ct += 1
                # 만약 마지막에 도달했다면 (마지막이 1로 끝난다면)
                if j == N - 1:
                    # 만약 카운트된 1값이 K라면
                    if ct == K:
                        cnt += 1
                        ct = 0
                    # 아니라면
                    else:
                        ct = 0
            # 좌표의 값이 1이 아니라면 (0이라면)
            else:
                # 이태까지 쌓인 ct 스택이 K와 같다면
                if ct == K:
                    cnt += 1
                    ct = 0
                # 아니라면
                else:
                    ct = 0

    # 세로 칸 수 세기
    for i in range(N):
        for j in range(N):
            if pz[j][i] == 1:
                ct += 1
                if j == N - 1:
                    if ct == K:
                        cnt += 1
                        ct = 0
                    else:
                        ct = 0
            else:
                if ct == K:
                    cnt += 1
                    ct = 0
                else:
                    ct = 0

    # 출력
    print(f'#{tc} {cnt}')