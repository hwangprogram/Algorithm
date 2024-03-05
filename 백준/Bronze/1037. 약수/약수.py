N = int(input())
N_lst = list(map(int, input().split()))

N_lst.sort()

ans = 0
if len(N_lst) == 1:
    ans = N_lst[0] ** 2
else:
    ans = N_lst[0] * N_lst[-1]

print(ans)