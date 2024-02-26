'''
SWEA 원 안의 점

문제 요약:
N이 주어질 때, 원점을 중심으로 반지름이 N인 원 안에 포함되는 격자점 (x, y 좌표가 모두 정수인 점)
의 개수를 구하는 프로그램을 작성하라
즉, x^2 + y^2 <= N^2인 격자점의 개수를 구하는 프로그램을 작성하라
'''
import math

T = int(input())

for tc in range(1, T+1):
    N = int(input())    # 반지름 N
    D = 2 * N           # 지름 D
    cnt = 0

    for x in range(-N, N+1):
        for y in range(-N, N+1):
            if x ** 2 + y ** 2 <= N ** 2:
                cnt += 1

    print(f'#{tc} {cnt}')
