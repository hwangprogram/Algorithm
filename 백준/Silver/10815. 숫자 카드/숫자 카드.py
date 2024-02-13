import sys

N = int(sys.stdin.readline())
N_lst = set(map(int, sys.stdin.readline().split()))

M = int(sys.stdin.readline())
M_lst = list(map(int, sys.stdin.readline().split()))

for i in M_lst:
    if i in N_lst:
        print(1, end=' ')
    else:
        print(0, end=' ')