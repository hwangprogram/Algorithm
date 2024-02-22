import sys

N, M = map(int, sys.stdin.readline().split())

poketmon_ntoi = {}
poketmon_iton = {}


for n in range(1, N+1):
    name = sys.stdin.readline().rstrip()
    poketmon_ntoi[name] = n
    poketmon_iton[n] = name

for m in range(M):
    q = sys.stdin.readline().rstrip()

    if q.isdigit():
        print(poketmon_iton[int(q)])
    else:
        print(poketmon_ntoi[q])