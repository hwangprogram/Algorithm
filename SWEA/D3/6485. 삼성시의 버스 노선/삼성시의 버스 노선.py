T = int(input())

for tc in range(1, T+1):
    N = int(input())    # N개의 노선

    bus_stop = [0] * 5001   # 5000개의 버스 정류장
    for n in range(N):
        A, B = map(int, input().split())    # A, B 사이를 지나는 노선

        for i in range(A, B+1):
            bus_stop[i] += 1                # A, B가 지나는 정류장들을 카운트

    P = int(input())    # P개의 정류장들

    print(f'#{tc}', end=' ')
    for p in range(P):
        C = int(input())
        print(bus_stop[C], end=' ')
    print()