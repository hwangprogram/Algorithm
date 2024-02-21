N = int(input())

i = 0
cnt = 0

while i < N:
    if (N - i) % 5 == 0:
        i += 5
        cnt += 1
    else:
        i += 3
        cnt += 1

if i == N:
    print(cnt)
else:
    print(-1)