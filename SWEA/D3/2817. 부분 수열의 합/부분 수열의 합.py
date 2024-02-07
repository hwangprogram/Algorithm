T = int(input())

for tc in range(1, T + 1):
    # 입력
    # N개의 자연수, 합이 K
    N, K = map(int, input().split())
    # N개의 자연수 list
    num_lst = list(map(int, input().split()))

    # 로직
    # 완전탐색을 통해, 가능한 모든 부분집합을 구하고, 그 중 합이 K인 것들을 카운트한다.
    n = len(num_lst)
    # 부분집합 중 합이 K인 것들 카운트할 변수
    cnt = 0
    for i in range(1 << n):     # 1<<n : 부분 집합의 개수
        # 부분집합을 담을 리스트
        sub_lst = []
        for j in range(n):      # 원소의 수만큼 비트를 비교한다.
            if i & (1 << j):    # i의 j번 비트가 1인 경우
                sub_lst.append(num_lst[j])

        if sum(sub_lst) == K:
            cnt += 1

    # 출력
    print(f'#{tc} {cnt}')