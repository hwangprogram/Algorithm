T = int(input())

for tc in range(1, T+1):
    # N 명의 사람, M초의 시간에 K개의 붕어빵 만듦
    N, M, K = map(int, input().split())

    '''
    M초마다 K개의 붕어빵
    그렇다면 X초에 붕어빵의 갯수는? X // M * K
    '''
    peoples = list(map(int, input().split()))
    peoples.sort()
    second = 0

    ans = 'Possible'
    sold_bread = 0
    for ppl in peoples:
        made_bread = (ppl // M) * K  # 지금까지 만든 빵의 갯수
        sold_bread += 1     # 팔린 빵 갯수 누적
        remain_bread = made_bread - sold_bread      # 재고
        if remain_bread < 0:
            ans = 'Impossible'
            break

    print(f'#{tc} {ans}')