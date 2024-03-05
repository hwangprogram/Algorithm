def factorial(n):
    global fac

    # 기저조건
    if n == 0:
        return

    fac *= n
    factorial(n-1)


N = int(input())
fac = 1
factorial(N)
print(fac)