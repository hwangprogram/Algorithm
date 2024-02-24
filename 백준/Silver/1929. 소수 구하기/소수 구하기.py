'''
# 1929 소수 구하기

문제 요약
M이상 N이하의 소수를 모두 출력하라
'''

def prime_num(m, n):
    seive = [True] * (n+1)

    h = int(n ** 0.5)
    for i in range(2, h+1):
        if seive[i] == True:
            for j in range(i+i, n+1, i):
                seive[j] = False

    seive[1] = False

    for num in range(m, n+1):
        if seive[num]:
            print(num)


M, N = map(int, input().split())

prime_num(M, N)