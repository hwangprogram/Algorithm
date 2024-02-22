import sys

N = int(sys.stdin.readline())

X_lst = list(map(int, sys.stdin.readline().split()))

no_dupe_x = sorted(list(set(X_lst)))
dict_lst = dict(zip(no_dupe_x, list(range(len(no_dupe_x)))))

for x in X_lst:
    print(dict_lst[x], end=' ')