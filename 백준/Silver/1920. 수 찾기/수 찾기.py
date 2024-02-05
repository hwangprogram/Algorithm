import sys

def binary_search(a, N, key):
    start = 0       # 정렬 시작지점
    end = N - 1     # 정렬 마지막지점
    while start <= end:     # start값이 end값보다 적을때 반복
        middle = (start + end) // 2     # 중앙값 탐색
        if a[middle] == key:    # 만약 a배열의 중앙값이 key값과 같다면,
            return True     # 검색 성공
        elif a[middle] > key:   # 만약 a배열의 중앙값이 key보다 크다면, 중앙값 미포함 중앙값보다 앞의 값을 end로 지정하여 다시 탐색
            end = middle - 1
        else:   # 만약 a배열의 중앙값이 kry보다 작다면, 중앙값 미포함 중앙값보다 뒤의 값을 start로 지정하여 다시 탐색
            start = middle + 1
    return False    # 검색 실패

# 입력
# N개의 정수 N_lst
N = int(sys.stdin.readline())
N_lst = list(map(int, sys.stdin.readline().split()))

# M개의 정수 M_lst
M = int(sys.stdin.readline())
M_lst = list(map(int, sys.stdin.readline().split()))

# 로직
# 자료 정렬
N_lst.sort()
# 이진탐색 함수를 통해 M_lst의 값을 하나하나 확인
for i in M_lst:
    if binary_search(N_lst, N, i):
        print(1)
    else:
        print(0)