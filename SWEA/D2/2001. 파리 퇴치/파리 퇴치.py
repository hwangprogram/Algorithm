T = int(input())

for tc in range(1, T + 1):
    # 입력
    # N x N 의 배열
    # M x M 의 크기를 가지는 파리채
    N, M = map(int, input().split())
    # N x N 크기를 가지는 배열 lst
    lst = [list(map(int, input().split())) for _ in range(N)]

    # 로직
    # M x M 크기의 배열이 N x N 배열의 내부를 순회하며 그 합을 카운트하는 변수 s_v
    # 카운트 된 값 중 최댓값을 가려내기 위한 변수 mx_v
    # M x M 크기의 파리채
    mx_v = s_v = 0
    for i in range(N - M + 1):
        for j in range(N - M + 1):
            s_v = 0
            for m in range(M):
                for n in range(M):
                    s_v += lst[i + m][j + n]
            if mx_v < s_v:
                mx_v = s_v

    print(f'#{tc} {mx_v}')