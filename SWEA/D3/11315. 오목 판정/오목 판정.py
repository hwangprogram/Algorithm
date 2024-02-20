dt = ((0, 1), (1, -1), (1, 0), (1, 1))  # 탐색할 4방향 (우, 좌하, 하, 우하)

def find(x, y, arr):        # 오목판정 함수
    for _x, _y in dt:       # 4방향 확인
        cnt = 1             # 2차원 리스트를 순회하며 돌을 찾은 것이므로, cnt를 1로 초기화 하고 시작
        for t in range(1, 5):   # 4칸 이동하며 탐색 -> 5목인지만 판정하면 되므로
            nx, ny = x + _x * t, y + _y * t # 이동할 좌표

            if 0 <= nx < N and 0 <= ny < N and arr[nx][ny] == 'o':      # 범위 내에 있고, 돌이 있다면,
                cnt += 1    # 카운트
                if cnt == 5:    # 오목을 찾았다면,
                    return 1
    else:               # 못 찾았다면 (for문을 다 돌았지만 찾지 못했다면)
        return 0


T = int(input())

for tc in range(1, T+1):
    N = int(input())    # NxN 크기의 판

    stage = [list(input()) for _ in range(N)]   # 판

    ans = 'NO'  # 찾았나 못찾았나
    escape = 0  # 탈출

    print(f'#{tc}', end=' ')
    for i in range(N):
        for j in range(N):          # 판 순회
            if stage[i][j] == 'o':  # 돌을 찾았을 때부터 탐색 시작
                if find(i, j, stage) == 1:  # 오목을 찾았으면,
                    ans = 'YES'
                    escape = 1
                    break
        if escape == 1:
            break

    print(ans)