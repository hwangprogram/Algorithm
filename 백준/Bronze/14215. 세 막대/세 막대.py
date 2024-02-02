a, b, c = map(int, input().split())

if max(a, b, c) >= a + b + c - max(a, b, c):
    if max(a, b, c) == a:
        a = b + c - 1
    elif max(a, b, c) == b:
        b = a + c - 1
    else:
        c = a + b - 1

print(a + b + c)