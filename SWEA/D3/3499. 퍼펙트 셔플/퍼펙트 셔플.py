'''
SWEA 퍼펙트 셔플

퍼펙트 셔플 : 카드 덱을 정확히 절반으로 나누고, 나눈 것들에서 교대로 카드를 뽑아 새로운 덱을
만드는 것
카드가 주어질 때, 퍼펙트 셔플하면 어떤 순서가 되는지 출력하라

설계
투 포인트 알고리즘
a = 맨 처음
b = 중간 + 1

Loop {
    a 출력 후 a + 1
    b 출력 후 b + 1
}
'''
T = int(input())
N = 0
arr = []


def get_result():
    a = 0
    b = (len(arr) + 1) // 2

    for turn in range(len(arr)):
        if turn % 2 == 0:
            print(arr[a], end=' ')
            a += 1
        else:
            print(arr[b], end=' ')
            b += 1


for tc in range(1, T+1):
    N = int(input())
    arr = list(map(str, input().split()))
    print(f'#{tc}', end=' ')
    get_result()
    print()