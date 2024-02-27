path = []
used = [False for _ in range(6)]

def triplet_b(arr):
    if arr[2] == arr[1] + 1 == arr[0] + 2:
        return True
    else:
        return False

def run_b(arr):
    if arr[0] == arr[1] == arr[2]:
        return True
    else:
        return False


def baby_gin(n, arr):
    global ans

    # 기저조건
    if n == 6:
        # 조건판별 (run, triplet)
        if (triplet_b(path[0:3]) or run_b(path[0:3])) and \
                (triplet_b(path[3:]) or run_b(path[3:])):
            ans = 'true'
        return

    for i in range(6):
        if used[i]: continue
        used[i] = True
        path.append(arr[i])
        baby_gin(n+1, arr)
        path.pop()
        used[i] = False


T = int(input())

for tc in range(1, T+1):
    N = list(map(int, input().rstrip()))

    ans = 'false'
    baby_gin(0, N)

    print(f'#{tc} {ans}')
