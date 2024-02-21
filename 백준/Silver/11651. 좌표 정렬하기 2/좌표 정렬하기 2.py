N = int(input())

location = []
for n in range(N):
    location.append(list(map(int, input().split())))

for l in location:
    l[0], l[1] = l[1], l[0]

location.sort()

for y, x in location:
    print(x, y)