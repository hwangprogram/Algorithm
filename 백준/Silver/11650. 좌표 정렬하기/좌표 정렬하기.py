N = int(input())

location = []
for n in range(N):
    location.append(tuple(map(int, input().split())))

location.sort()

for x, y in location:
    print(x, y)