'''
SWEA 스도쿠 검증

문제 요약:
가로 9칸, 세로 9칸의 표가 주어진다.
가로, 세로, 내부의 3x3 배열에는 1~9까지의 숫자가 중복없이 있어야 한다.
중복되거나, 없는 수가 있다면 스도쿠를 만족하지 못하는 것
만족하면 1, 못하면 0 출력
'''

T = int(input())

for tc in range(1, T+1):
    puzzle = [list(map(int, input().split())) for _ in range(9)]

    sudoku = [0] * 10
    ans = 1
    # 가로 검증
    for i in range(9):
        for j in range(9):
            sudoku[puzzle[i][j]] += 1
        if sudoku.count(1) < 9: # 1이 9개 없다면(중복되거나, 없는값이 있다면)
            ans = 0
            break
        sudoku = [0] * 10   # 초기화

    # 세로검증
    for j in range(9):
        for i in range(9):
            sudoku[puzzle[i][j]] += 1
        if sudoku.count(1) < 9:  # 1이 9개 없다면(중복되거나, 없는값이 있다면)
            ans = 0
            break
        sudoku = [0] * 10  # 초기화

    # 3x3 검증
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            for k in range(i, i+3):
                for l in range(j, j+3):
                    sudoku[puzzle[k][l]] += 1
            if sudoku.count(1) < 9:  # 1이 9개 없다면(중복되거나, 없는값이 있다면)
                ans = 0
                break
            sudoku = [0] * 10  # 초기화

    print(f'#{tc} {ans}')