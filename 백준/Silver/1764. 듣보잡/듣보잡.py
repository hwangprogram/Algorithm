N, M = map(int, input().split())

listen = set()
see = set()
listen_see = set()

for n in range(N):
    listen.add(input())

for m in range(M):
    see.add(input())

listen_see = listen & see

srted_lst = sorted(list(listen_see))

print(len(listen_see))
for i in srted_lst:
    print(i)