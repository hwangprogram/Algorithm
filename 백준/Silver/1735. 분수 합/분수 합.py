def sub(a, b):
    while b != 0:
        r = a % b
        a = b
        b = r
    return a


A_c, A_m = map(int, input().split())
B_c, B_m = map(int, input().split())

sub_m = sub(A_m, B_m)
AB_m = A_m * B_m // sub_m
AB_c = 0

if sub_m != 0:
    AB_c = (A_c * (AB_m // A_m)) + (B_c * (AB_m // B_m))

devide = sub(AB_c, AB_m)

print(AB_c // devide, AB_m // devide)