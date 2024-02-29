'''
SWEA 백만장자 프로젝트

문제 요약:
1. 원재는 연속된 N일 동안의 물건의 매매가를 예측하여 알고 있다.
2. 당국의 감시망에 걸리지 않기 위해 하루에 최대 1만큼 구입할 수 있다.
3. 판매는 얼마든지 할 수 있다.

전략:
1. 뒤에서부터 순회하기 시작
2. 순회하면서 스택에 나보다 큰 값을 넣는다
3. 뒤에 있는 값이 나보다 작으면 판다.
4. 뒤에 있는 값이 나보다 크면 그 값으로 교체한다.
'''
T = int(input().rstrip())

for tc in range(1, T+1):
    N = int(input().rstrip())
    N_lst = list(map(int, input().rstrip().split()))   # N개의 매매가

    mx_n = 0
    sm_n = 0
    for n in range(N-1, -1, -1):
        if N_lst[n] > mx_n:
            mx_n = N_lst[n]
        else:
            sm_n += (mx_n - N_lst[n])

    print(f'#{tc} {sm_n}')