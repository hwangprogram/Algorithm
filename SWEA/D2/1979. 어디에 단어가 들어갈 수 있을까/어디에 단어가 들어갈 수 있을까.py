T = int(input())

for tc in range(1, T + 1):
    # 입력
    # 가로, 세로 길이 N, 단어의 길이 K
    N, K = map(int, input().split())

    # 퍼즐 pz
    pz = [list(map(int, input().split())) for _ in range(N)]

    # 로직
    # 가로에 대해 연속된 1 찾기, 세로에 대해 연속된 1 찾기 시행
    # 길이가 K인지 확인할 변수 is_k, 길이세는 변수 cnt
    is_k = cnt = 0

    # 가로
    for i in range(N):
        for j in range(N):
            if pz[i][j] == 1:
                cnt += 1
                if j == N - 1:
                    if cnt == K:
                        is_k += 1
                    cnt = 0
            else:
                if cnt == K:
                    is_k += 1
                cnt = 0

    # 세로
    for j in range(N):
        for i in range(N):
            if pz[i][j] == 1:
                cnt += 1
                if i == N - 1:
                    if cnt == K:
                        is_k += 1
                    cnt = 0
            else:
                if cnt == K:
                    is_k += 1
                cnt = 0

    # 출력
    print(f'#{tc} {is_k}')