import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    a, b = map(int, input().split())

    if pow(a, b, 10) == 0:
        print(10)
    else:
        print(pow(a, b, 10))