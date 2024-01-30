N = int(input())
ans = i = 0
spot = 2

while i != N:
    spot = spot * 2 - 1
    ans = spot ** 2
    i += 1

print(ans)