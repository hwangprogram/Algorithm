T = 4
arr = [[0] * 101 for _ in range(101)]
sm = 0

for _ in range(T):
    lx, ly, rx, ry = map(int, input().split())

    for i in range(ly, ry):
        for j in range(lx, rx):
            arr[i][j] = 1
for i in range(101):
    sm += sum(arr[i])

print(sm)