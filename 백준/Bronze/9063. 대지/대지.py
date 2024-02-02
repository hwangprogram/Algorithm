N = int(input())

max_x = max_y = -10000
min_x = min_y = 10000

for i in range(N):
    x, y = map(int, input().split())

    if N > 1:
        max_x = max(x, max_x)
        max_y = max(y, max_y)
        min_x = min(x, min_x)
        min_y = min(y, min_y)
    else:
        max_x = min_x = max_y = min_y = 0

area = (max_x - min_x) * (max_y - min_y)

print(area)