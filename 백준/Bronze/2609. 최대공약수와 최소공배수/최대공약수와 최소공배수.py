# 최대 공약수: 유클리드 호재법
def gcd(a, b):
    # a를 b로 나누어서 b를 a에, 나눈 나머지를 b에 대입시켜 b가 0이 될때까지 반복하면
    # 남는 a값이 최대 공약수이다.
    while b > 0:
        a, b = b, a % b
    return a

# 최소 공배수: 두 수를 곱한 값에서 최대 공약수로 나눈 값
def lcm(a, b):
    return a * b // gcd(a, b)


# 두 자연수 A, B
A, B = map(int, input().split())

if A > B:
    print(gcd(A, B))
    print(lcm(A, B))
else:
    print(gcd(B, A))
    print(lcm(A, B))


