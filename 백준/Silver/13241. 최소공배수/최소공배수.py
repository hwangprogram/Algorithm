import sys


def least_sub(a, b):
    while b != 0:
        r = a % b
        a = b
        b = r
    return a


A, B = map(int, sys.stdin.readline().split())

R = least_sub(A, B)
print(A * B // R)