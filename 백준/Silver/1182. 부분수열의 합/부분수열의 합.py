'''
#1182 부분수열의 합
문제 요약
N개의 정수로 이루어진 수열이 있을 때,
수열의 원소를 다 더한 값이 S가 되는 경웃의 수를 구하는 프로그램 작성
'''

N, S = map(int, input().split())
N_lst = list(map(int, input().split()))
result = []
total = 0

def dfs(idx, sm):
    '''
    :param idx: 인덱스 (인자의 갯수)
    :param sm: 숫자들의 합
    :return: x, total에 1식 추가
    '''
    global total    # 부븐수열의 개수

    # 기저조건 : 원소의 합이 S가 되었을 때, 혹은 원소 수 이상이 되었을 때
    if idx >= N:
        return

    sm += N_lst[idx]

    if sm == S:
        total += 1

    # 다음 원소를 추가 했을 때
    dfs(idx+1, sm)
    
    # 다음 원소를 추가하지 않았을 때
    dfs(idx+1, sm - N_lst[idx])


dfs(0, 0)
print(total)