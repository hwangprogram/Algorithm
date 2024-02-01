def rotate(N, arr):
    lst = [list(tp) for tp in zip(*arr)]
    for i in range(N):
        lst[i].reverse()
    return lst

def to_string(N, lst):
    st = ''
    for i in range(N):
        st += str(lst[i])
    return st

# 입력
T = int(input())

for tc in range(1, T + 1):
    N = int(input())

    arr = [list(map(int, input().split())) for _ in range(N)]

    print(f'#{tc}')
    for i in range(N):
        ans_90 = rotate(N, arr)
        ans_180 = rotate(N, ans_90)
        ans_270 = rotate(N, ans_180)
        s_9 = to_string(N, ans_90[i])
        s_18 = to_string(N, ans_180[i])
        s_27 = to_string(N, ans_270[i])

        print(s_9, s_18, s_27)