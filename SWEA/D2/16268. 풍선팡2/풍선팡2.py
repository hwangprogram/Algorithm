T = int(input())

for tc in range(1, T + 1):
    #  입력
    # N x M 개의 풍선
    N, M = map(int, input().split())

    # 풍선들 balloons
    balloons = [list(map(int, input().split())) for _ in range(N)]

    # 로직
    # 추가로 터트려줄 풍선들의 델타값
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]

    # 합 sum_v, 최댓값 mx_v
    sum_v = mx_v = 0

    # 풍선 순회
    for i in range(N):
        for j in range(M):
            sum_v = 0
            sum_v += balloons[i][j]
            for k in range(4):
                ni = i + di[k]
                nj = j + dj[k]
                if ni >= 0 and ni < N and nj >= 0 and nj < M:
                    sum_v += balloons[ni][nj]
            if mx_v < sum_v:
                mx_v = sum_v

    # 출력
    print(f'#{tc} {mx_v}')