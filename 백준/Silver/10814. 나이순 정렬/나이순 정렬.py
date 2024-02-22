N = int(input())

order_member = [[] for _ in range(N)]

for n in range(1, N + 1):
    mem = input().split()
    mem[0] = int(mem[0])
    mem.append(n)

    order_member[n-1] = mem

order_member.sort(key=lambda x: (x[0], x[2]))

for n in range(N):
    print(order_member[n][0], order_member[n][1])