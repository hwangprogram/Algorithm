import sys

def gcd(a, b):
    while b != 0:
        r = a % b
        a = b
        b = r
    return a


N = int(sys.stdin.readline())

tree_lst = []
dif_lst = []

for n in range(N):
    tree = int(sys.stdin.readline().rstrip())
    tree_lst.append(tree)

for i in range(N-1):
    dif_lst.append(tree_lst[i+1] - tree_lst[i])

distance = 0

if len(dif_lst) == 1:
    distance = dif_lst[0]
else:
    distance = dif_lst[0]
    for dif in dif_lst[1:]:
        distance = gcd(distance, dif)

cnt = ((tree_lst[-1] - tree_lst[0]) // distance) + 1 - N

print(cnt)