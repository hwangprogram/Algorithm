'''
백준 15711 환상의 짝꿍

문제요약:
두 사람의 끈의 길이가 테스트케이스 수 만큼 주어진다.
이 끈을 이어 붙인 길이가 소수인 두개의 끈으로 나눌 수 있다면, 이들은 환상의 짝꿍이다.

전략:
제한시간이 1초이고, 입력이 10의 12승 까지 주어진다.
즉, 이 문제는 O(N) 이하의 시간복잡도로 풀어야 한다.
A + B의 최대 값은 4x10^12 이다.
A + B 이하의 소수는 A + B 를 제곱근 한 수 이하의 소수로 나누어지지 않는 수이다.
'''
import sys
input = sys.stdin.readline

N = 2 * 10 ** 6
seive = [True] * (N + 1)
primes = []

# 에라토스테네스의 체 사용
seive[0] = seive[1] = False

for i in range(2, N+1):
    if seive[i]:
        primes.append(i)
    for j in range(i+i, N+1, i):
        seive[j] = False


# 테스트케이스 수
T = int(input())

for _ in range(T):
    # 두 사람이 가진 끈의 길이 n1, n2
    n1, n2 = map(int, input().split())

    test = n1+n2

    # 두 수의 합이 2 또는 3 이면 => 소수의 합으로 표현 x
    if test == 2 or test == 3:
        print('NO')
        continue

    # 두 수의 합이 짝수: 골드바흐의 추측에 따라 두 수의 합이 짝수라면 소수인 두개 수로 나눌 수 있다.
    if test % 2 == 0:
        print('YES')
    # 두 수의 합이 홀수: 홀수는 반드시 짝수 + 홀수이다.
    # 그런데 짝수 중 소수는 2밖에 없으므로 두 수를 더한 값 - 2가 소수이면 된다.
    else:
        # 구하려는 값이 N보다 작다면
        if test+2 <= N:
            if seive[test-2]:
                print('YES')
            else:
                print('NO')
        # 아니라면
        else:
            # 소수인지 판별
            for i in primes:
                # 소수로 나눠진다면
                if (test-2) % i == 0:
                    print('NO')
                    break

            # 안나눠졌다면
            else:
                print("YES")
