T = int(input())
for test_case in range(1, T + 1):
    '''
    반복문 종료 조건 : N*N 수치 할당 혹은 달팽이가 정중앙
    회전 순서 : 우측, 하강, 좌측, 상승 loop
    회전 조건 : 배열 바깥으로 탈출
                할당된 값이 존재할 경우 if !=0 이런거
    '''
    # 델타 탐색 만들기, 체스말 문제, 그림으로 그리는 거 추천
    # 팔방 탐색 문제 많이 나옴
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    # 시계 방향 순회
    N = int(input())

    arr = [[0] * N for _ in range(N)]

    # logic for/while 작성
    cnt = 1
    dr = 0
    # 달팽이 좌표 설정, 좌에서 우로 읽는 구조라 턱이 걸리는거 없도록
    i, j = 0, 0
    while True:
        # 달팽이가 보는 방향
        arr[i][j] = cnt
        if cnt == N * N:
            break
        # 달팽이 시프트
        ni = i + di[dr]
        nj = j + dj[dr]
        # 단축 평가 유도
        if 0 > ni or N <= ni or 0 > nj or N <= nj or arr[ni][nj] != 0:
            dr = (dr + 1) % 4
            continue
        i, j = ni, nj
        cnt += 1
    print(f'#{test_case}')
    # 왜 빼는지 알아야함
    for i in range(N):
        print(*arr[i])