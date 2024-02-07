T = int(input())

for tc in range(1, T + 1):
    N = int(input())

    paskal = [[] for _ in range(N)]

    for i in range(N):
        for j in range(0, i + 1):
            if i == 0 or j == 0 or i == j:
                paskal[i].append(1)
            else:
                paskal[i].append(paskal[i - 1][j] + paskal[i - 1][j - 1])

    print(f'#{tc}')
    for i in range(N):
        print(*paskal[i])