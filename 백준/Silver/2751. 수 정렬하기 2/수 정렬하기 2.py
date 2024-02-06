import sys

N = int(sys.stdin.readline())
num_lst = []

for i in range(N):
    num_lst.append(int(sys.stdin.readline()))

num_lst.sort()
for j in num_lst:
    print(j)