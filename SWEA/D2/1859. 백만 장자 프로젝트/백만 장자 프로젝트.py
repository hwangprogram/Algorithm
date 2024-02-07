T = int(input())

for tc in range(1, T + 1):
    # 입력
    # N개의 가격 cost
    N = int(input())
    cost = list(map(int, input().split()))

    # 판매액 합
    sum_cost = 0

    if cost.index(max(cost)) != 0:
         while cost != []:
            sell_idx = cost.index(max(cost))
            sum_cost += max(cost) * len(cost[:sell_idx]) - sum(cost[:sell_idx])
            cost[:sell_idx + 1] = []

    print(f'#{tc} {sum_cost}')