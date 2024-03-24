def make_subset(idx, sm):
    global cnt

    # 가지치기: 합이 K초과 되면 종료
    if sm > K:
        return

    # 기저조건: idx가 N이상 되면 종료
    if idx == N:
        # 정답조건: sm이 K이면 정답처리
        if sm == K:
            cnt += 1
        return

    # 재귀조건: sm에 다음 원소를 더하는가, 더하지 않는가
    # 더한다.
    make_subset(idx+1, sm+A[idx])
    # 더하지 않는다
    make_subset(idx+1, sm)


T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    cnt = 0
    make_subset(0, 0)
    print(f"#{tc} {cnt}")