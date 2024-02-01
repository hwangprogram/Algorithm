# 입력
# 소인수 분해를 시행할 값 N
N = int(input())

while N > 1:
    for i in range(2, N + 1):
        if N % i == 0:
            N //= i
            print(i)
            break