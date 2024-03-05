T = int(input())

for _ in range(1, T+1):
        K, N = map(int, input().split())

        n_fac = 1
        n_k_fac = 1
        k_fac = 1

        n = N
        n_k = N-K
        k = K
        while n != 0:
            n_fac *= n
            n -= 1

        while n_k != 0:
            n_k_fac *= n_k
            n_k -= 1

        while k != 0:
            k_fac *= k
            k -= 1

        print(n_fac//(n_k_fac * k_fac))