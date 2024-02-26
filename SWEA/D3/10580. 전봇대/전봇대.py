'''
SWEA 전봇대

설계
A - B를 잇는 경우
1 ~ (A-1) 사이에, B보다 큰 것을 Counting
    - 만약 아래 상태에서 4 - 1을 잇는 경우,
    1 ~ 3 사이에 3보다 큰 것을 Counting
'''

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    A_lst, B_lst = [], []
    cnt = 0

    for n in range(N):
        A, B = map(int, input().split())

        A_lst.append(A)
        B_lst.append(B)

    for n1 in range(N):
        for n2 in range(n1+1, N):
            if A_lst[n1] < A_lst[n2] and B_lst[n1] < B_lst[n2]:
                continue
            elif A_lst[n1] > A_lst[n2] and B_lst[n1] > B_lst[n2]:
                continue
            else:
                cnt += 1

    print(f'#{tc} {cnt}')

# ----------------------------------------------------------------------
# 강사님 풀이

# def get_result():
#     size = len(arr)
#     cnt = 0
#     for i in range(size):
#         for tar in range(i):
#             # a 전봇대 : 튜플의 첫 번째 요소, b 전봇대 : 튜플의 두번째 요소
#             i_a, i_b = (arr[i][0], arr[i][1])
#             tar_a, tar_b = (arr[tar][0], arr[tar][1])
#             if i_b < tar_b:
#                 cnt += 1
#     return cnt
#
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     arr = []
#     for n in range(N):
#         a, b = map(int, input().split())
#         # 튜플 형태로 a전봇대와 b전봇대를 append
#         arr.append((a, b))
#
#     arr.sort(key = lambda x: x[1]) # 첫 번째 원소를 기준으로, 오름차순 정렬
#     result = get_result()
#     print(f'#{tc} {result}')