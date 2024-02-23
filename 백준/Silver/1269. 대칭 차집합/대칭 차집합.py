A, B = map(int, input().split())

A_set = set(map(int, input().split()))
B_set = set(map(int, input().split()))

A_B_dif = A_set.difference(B_set)
B_A_dif = B_set.difference(A_set)

print(len(A_B_dif) + len(B_A_dif))