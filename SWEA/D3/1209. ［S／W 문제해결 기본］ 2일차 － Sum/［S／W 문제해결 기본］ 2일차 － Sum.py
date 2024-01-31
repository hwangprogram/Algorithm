T = 10

for tc in range(1, T + 1):
    # 입력
    # 첫 줄 테스트 케이스 번호 test_case
    test_case = int(input())
    # 100 x 100의 크기를 가지는 배열 arr
    arr = [list(map(int, input().split())) for _ in range(100)]

    # 로직
    # i단을 순회하며 행들의 합산 산출
    # j단을 순회하며 열들의 함산 산출
    # 대각선 2방향의 합산 산출
    # 각 합을 저장하는 변수 sum_v
    sum_v = 0
    # 최댓값을 저장하는 mx_v 변수
    mx_v = 0

    # 행들의 합
    for i in range(100):
        sum_v = sum(arr[i])
        if mx_v < sum_v:
            mx_v = sum_v

    sum_v = 0

    # 열들의 합
    for i in range(100):
        for j in range(100):
            sum_v += arr[j][i]
        if mx_v < sum_v:
            mx_v = sum_v
        sum_v = 0


    # 대각선의 합 (우하향)
    for i in range(100):
        for j in range(100):
            if i == j:
                sum_v += arr[i][j]

    if mx_v < sum_v:
        mx_v = sum_v

    sum_v = 0

    # 대각선의 합 (좌하향)
    for i in range(100):
        for j in range(100):
            if i + j == 100:
                sum_v += arr[i][j]

    if mx_v < sum_v:
        mx_v = sum_v

    # 출력
    print(f'#{tc} {mx_v}')