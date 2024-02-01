# 입력
# M 이상 N 이하의 자연수
M = int(input())
N = int(input())

# 로직
# M이상 N이하의 자연수중 소수들의 합을 구하는 변수 sb_sm, 소수의 최솟값 sb_mn
dec_sm = dec_mn = 0

# 소수 리스트 sub_lst
dec_lst = []

# 소수인가 아닌가
is_dec = 0

# M과 N사이 숫자들을 순회하며 소수를 찾음
for i in range(M, N + 1):
    each_sub = []
    for j in range(1, i + 1):
        if i % j == 0:
            each_sub.append(j)
    if len(each_sub) == 2:
        dec_lst.append(i)

# 소수들의 합
if len(dec_lst) != 0:
    dec_sm = sum(dec_lst)

# 제일 작은 소수
if len(dec_lst) != 0:
    dec_mn = min(dec_lst)

# 소수가 없는 경우를 상정
if len(dec_lst) == 0:
    print(-1)
else:
    print(dec_sm)
    print(dec_mn)