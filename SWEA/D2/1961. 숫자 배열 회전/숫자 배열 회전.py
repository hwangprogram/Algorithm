T = int(input())

# 전치해주고 뒤집어주는 함수 rotate
def rotate(n, arr):
    lst = [list(tp) for tp in zip(*arr)]

    for i in range(n):
        lst[i].reverse()

    for i in range(n):
        for j in range(n):
            lst[i][j] = str(lst[i][j])

    return lst


for tc in range(1, T + 1):
    # 입력
    # N x N 행렬
    N = int(input())

    # 행렬 mat
    mat = [list(map(int, input().split())) for _ in range(N)]

    # 논리
    # 돌려주고 뒤집어주는 함수 rotate 정의

    orginal_mat = mat

    # 출력
    print(f'#{tc}')
    for i in range(N):
        for j in range(3):
            mat = rotate(N, mat)
            print(''.join(mat[i]), end=' ')
        mat = orginal_mat
        print()