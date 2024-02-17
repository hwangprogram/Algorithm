dt = ((1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1))  # 8방향 탐색


def search(arr):
    for x in range(N):  # 오목판 순회
        for y in range(N):
            if arr[x][y] == 'o':  # o를 찾으면 탐색 시작
                for _x, _y in dt:  # 우선 방향 선택
                    cnt = 1
                    for k in range(1, 5):  # 5번 이동하며 탐색
                        nx, ny = x + _x * k, y + _y * k

                        if 0 <= nx < N and 0 <= ny < N and arr[nx][ny] == 'o':  # 범위 내에 있고 찾는 값이라면
                            cnt += 1
                            if cnt == 5:  # 돌이 5개 이상 연속하면
                                return 'YES'
    else:
        return 'NO'


T = int(input())

for tc in range(1, T + 1):
    N = int(input())  # 오목판의 크기 NxN
    rock = [list(input()) for _ in range(N)]  # 오목판

    cnt = 0

    print(f'#{tc} {search(rock)}')