import sys
from collections import Counter

cnt = 0
N = int(sys.stdin.readline().rstrip())
N_lst = list(map(int, sys.stdin.readline().split()))

M = int(sys.stdin.readline().rstrip())
M_lst = list(map(int, sys.stdin.readline().split()))

c = Counter(N_lst)

for m in M_lst:
    if m in c:
        print(c[m], end=' ')
    else:
        print(0, end=' ')