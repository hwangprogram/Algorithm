N, M = map(int, input().split())

num_lst = list(map(int, input().split()))
sum_lst = []
sub_lst = []
min_num = 300000

for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            sum_lst.append(num_lst[i]+num_lst[j]+num_lst[k])

for num in sum_lst:
    sub_lst.append(M-num)
    if M-num >= 0:
        min_num = min(min_num, M-num)

min_idx = sub_lst.index(min_num)

print(sum_lst[min_idx])

