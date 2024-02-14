# n명의 사람, k 번째 사람
n, k = map(int, input().split())

# 사람들 lst
ppl_lst = list(range(1, n+1))

# k번쨰 사람들 넣어줄 list
k_lst = []

# 인덱스 좌표
index = 0

while ppl_lst:
    index += k - 1  # 하나씩 줄기 때문에
    if index > len(ppl_lst) - 1:    # 인덱스 범위를 벗어난다면
        while index > len(ppl_lst) - 1:    # index값이 사람들 lst의 인덱스 최대값보다 작을 때 까지
            if len(ppl_lst) != 1:
                index -= len(ppl_lst)
            else:
                index = 0

    k_lst.append(ppl_lst.pop(index))

print('<', end='')
for i in range(n - 1):
    print(k_lst[i], end=', ')
print(k_lst[n - 1], end='>')