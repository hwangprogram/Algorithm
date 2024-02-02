T = int(input())

for tc in range(1, T + 1):
    # 입력
    # 배열의 한변의 길이 N
    # 파리채 한변 길이 M
    N, M = map(int, input().split())

    # 배열 arr
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 로직
    # 배열을 순회
    # 배열 내부에서 파리채의 면적만큼 순회하며 퇴치한 파리수 더하기
    # 합 변수 sum_v, 최대 합 mx_sum
    sum_v = mx_sum = 0

    for i in range(N):
        for j in range(N):
            sum_v = 0
            for k in range(M):
                for l in range(M):
                    if i + k < N and j + l < N:
                        sum_v += arr[i + k][j + l]
            mx_sum = max(mx_sum, sum_v)

    # 출력
    print(f'#{tc} {mx_sum}')