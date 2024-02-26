'''
기차 사이의 파리

두 기차가 부딪히기 전까지 소모된 시간 동안 파리가 움직인 거리를 구하면 되는 문제

- 파리의 속도 = F 이므로, 정답은 F x T 가 된다.
- T = 250 / (A + B) * F
'''

T = int(input())

for tc in range(1, T+1):
    D, A, B, F = map(int, input().split())

    ans = (D * F) / (A + B)

    print(f'#{tc} {ans}')