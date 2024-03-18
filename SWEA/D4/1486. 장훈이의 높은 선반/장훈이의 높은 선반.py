'''
높이가 B와 가장 비슷한 수열의 합을 찾는 문제
모든 수열을 만들어서 그 중 B와의 차이가 가장 작은 값을 return한다.
단, 수열은 중복 x
'''

# 수열 만들기
def make_set(i, sm):
    global min_sm

    # 기저조건: 가능한 인덱스 초과하면 return
    if i == N:
        if sm >= B:
            if sm < min_sm:
                min_sm = sm
        return

    make_set(i+1, sm+N_lst[i])
    make_set(i+1, sm)


T = int(input())

for tc in range(1, T+1):
    N, B = map(int, input().split())
    N_lst = list(map(int, input().split()))

    min_sm = 200000
    visited = [0]*(N+1)

    make_set(0, 0)

    print(f'#{tc} {min_sm-B}')