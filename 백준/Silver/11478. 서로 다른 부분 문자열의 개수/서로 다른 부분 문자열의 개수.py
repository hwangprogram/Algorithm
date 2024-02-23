S = input()
N = len(S)

sub_lst = []

for i in range(1, N+1):     # 갯수가 j개인 부분집합 (슬라이싱)
    for j in range(N-i+1):
        sub_lst.append(S[j:j+i])

sub_lst = list(set(sub_lst))

print(len(sub_lst))