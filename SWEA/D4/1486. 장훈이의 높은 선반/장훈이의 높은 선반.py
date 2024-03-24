def make_set(idx, sm):
    global mn_sm

    # 기저조건: 인덱스 값이 N초과 시 종료
    if idx == N:
        if sm >= B:
            mn_sm = min(sm, mn_sm)
        return

    # 재귀조건: 다음 인덱스를 포함하냐, 하지 않느냐
    make_set(idx+1, sm+heights[idx])
    make_set(idx+1, sm)


T = int(input())

for tc in range(1, T+1):
    N, B = map(int, input().split())

    heights = list(map(int, input().split()))

    mn_sm = 200000
    make_set(0, 0)

    print(f"#{tc} {mn_sm - B}")
