T = int(input())

for tc in range(1, T + 1):
    # 입력
    # N개의 행, M개의 열
    # 입력받는 2차원 배열 lst
    N, M = map(int, input().split())
    lst = [list(map(int, input().split())) for _ in range(N)]

    # 로직
    # 상하좌우 델타값을 입력 di, dj
    # 2차원 리스트를 순회하며 값 더함
    # 합을 입력받는 변수 sum_v
    # 그중 최댓값을 입력받는 변수 mx_v
    di = [0, 1, 0, -1, 0]
    dj = [0, 0, 1, 0, -1]
    sum_v = mx_v = 0

    for i in range(N):
        for j in range(M):
            sum_v = 0
            for k in range(5):
                ni = i + di[k]
                nj = j + dj[k]
								# 인덱스 에러 방지
                if 0 <= ni < N and 0 <= nj < M:
                    sum_v += lst[ni][nj]
						# mx_v값이 sum_v값보다 작다면 mx_v를 sum_v값으로 치환 (최대값 구하기)
            if mx_v < sum_v:
                mx_v = sum_v


    # 출력
    print(f'#{tc} {mx_v}')