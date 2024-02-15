# from collections import deque

T = int(input())    # 테스트케이스의 수 T

for tc in range(1, T+1):
    N, M = map(int, input().split())    # 문서의 개수 N

    que = list(enumerate(map(int, input().split())))

    cnt = 0     # 출력될때마다 세어주는 카운트

    while que:
        mx_v = max(que, key=lambda x: x[1])[1]      # que의 두번째 인덱스(값)을 기준으로 최댓값을 선정

        if que[0][1] < mx_v:    # 첫번째 인덱스의 값이 최댓값보다 작다면
            que.append(que.pop(0))      # 맨 앞의 값을 꺼내서 뒤로 추가 (rotate와 비슷)
        else:                   # 최댓값이라면,
            goal = que.pop(0)   # pop해준다.
            cnt += 1            # 출력되었으니 cnt + 1

            # 기저 조건: 목표 인덱스(M)을 만났다면, 그 인덱스를 print 해주고 반복문을 종료한다.
            if goal[0] == M:    # pop된 값의 인덱스가 M이라면
                print(cnt)      # 지금까지 몇개가 pop되었는지(나온 순서)를 출력
                break           # 반복문을 빠져나옴
