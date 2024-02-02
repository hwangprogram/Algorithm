T = int(input())

for tc in range(1, T + 1):
    # 입력
    # 버스노선의 수 N
    N = int(input())

    # 각 버스가 지나가는 정류장 : A ~ B
    AB_lst = []

    for _ in range(N):
        AB_lst.append(list(map(int, input().split())))

    # P개의 버스 정류장
    P = int(input())

    # 각 정거장 리스트
    station = [0] * P

    # 각 정류장 C
    for j in range(P):
        C = int(input())
        for i in AB_lst:
            if C >= i[0] and C <= i[1]:
                station[j] += 1

    # 로직
    # C를 입력 받으며 A 보다 크고, B보다 작다면 C를 지나가는 리스트 station에 append

    # 출력
    print(f'#{tc}', *station)