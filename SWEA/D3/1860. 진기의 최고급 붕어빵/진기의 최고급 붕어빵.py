T = int(input())

for tc in range(1, T+1):
    # N명의 사람, M초마다 K개의 붕어빵 만듦
    N, M, K = map(int, input().split())

    # 도착하는 사람들
    arrive_ppl = list(map(int, input().split()))

    # 정렬
    arrive_ppl.sort()

    arrive_ppl.append(0)

    # 초별 붕어빵 변수 (증가함)
    dorayakki = 0

    # 붕어빵 조달 가능한가
    ans = 'Possible'

    i = 0
    for j in range(max(arrive_ppl) + 1):
        # M의 배수 초 마다 붕어빵 만들기
        if j % M == 0:
            if j == 0:
                continue
            else:
                dorayakki += K

        if arrive_ppl[i] == 0:
            ans = 'Impossible'
            break

        # 사람이 올때마다 붕어빵 내어줌
        while j == arrive_ppl[i]:
            if dorayakki < 1:
                ans = 'Impossible'
                break
            else:
                dorayakki -= 1
            i += 1

        if ans == 'Impossible':
            break

    print(f'#{tc} {ans}')