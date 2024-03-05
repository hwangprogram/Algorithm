import sys
from collections import deque
input = sys.stdin.readline

N = int(input())

deq = deque()
for n in range(N):
    order = list(map(int, input().split()))

    if order[0] == 1:
        deq.appendleft(order[1])
    elif order[0] == 2:
        deq.append(order[1])
    elif order[0] == 3:
        if len(deq) == 0:
            print(-1)
        else:
            print(deq.popleft())
    elif order[0] == 4:
        if len(deq) == 0:
            print(-1)
        else:
            print(deq.pop())
    elif order[0] == 5:
        print(len(deq))
    elif order[0] == 6:
        if len(deq) == 0:
            print(1)
        else:
            print(0)
    elif order[0] == 7:
        if len(deq) == 0:
            print(-1)
        else:
            print(deq[0])
    elif order[0] == 8:
        if len(deq) == 0:
            print(-1)
        else:
            print(deq[-1])