T = int(input())

for tc in range(1, T + 1):
    # 입력
    # 9 x 9 크기의 퍼즐 데이터 puzzle
    puzzle = [list(map(int, input().split())) for _ in range(9)]

    # 로직
    # 확인해야 하는 것은 총 3가지
    # 1. 가로줄 내에서 겹치지 않는가
    # 2. 세로줄 내에서 겹치지 않는가
    # 3. 3 x 3 행렬 내에서 겹치지 않는가
    # 가로줄에서 1 ~ 9 숫자의 중복성을 평가할 변수 is_dup
    is_dup = 0

    # 1 ~ 9를 세어줄 리스트 cnt_lst
    cnt_lst = [0] * 9

    # 정답 True, False값을 판별해줄 값 ans
    ans = 1

    # 가로줄의 길이만큼 반복문을 통해 count 1 ~ 9
    for i in range(1, 10):
        for j in range(1, 10):
            if j in puzzle[i - 1]:
                cnt_lst[j - 1] += 1

        for cnt in cnt_lst:
            if cnt != 1:
                ans = 0
                break
        cnt_lst = [0] * 9

    cnt_lst = [0] * 9

    # 세로줄 평가
    # 세로줄로 새로운 lst 생성
    ver_pz = [list(tp) for tp in zip(*puzzle)]

    for i in range(1, 10):
        for j in range(1, 10):
            if j in ver_pz[i - 1]:
                cnt_lst[j - 1] += 1

        for cnt in cnt_lst:
            if cnt != 1:
                ans = 0
                break
        cnt_lst = [0] * 9

    cnt_lst = [0] * 9

    # 3 x 3 행렬 평가
    for i in range(0, 7, 3):
        for j in range(0, 7, 3):
            for k in range(3):
                for l in range(3):
                    if puzzle[i + k][j + k] in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
                        cnt_lst[puzzle[i + k][j + l] - 1] += 1

            for cnt in cnt_lst:
                if cnt != 1:
                    ans = 0
                    break
            cnt_lst = [0] * 9

    # 출력
    print(f'#{tc} {ans}')