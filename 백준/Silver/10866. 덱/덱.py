import sys

N = int(sys.stdin.readline())
deque = []

for tc in range(N):

    commend = sys.stdin.readline().split()

    if commend[0] == 'push_front':
        deque.insert(0, commend[1])
    elif commend[0] == 'push_back':
        deque.append(commend[1])
    elif commend[0] == 'pop_front':
        if len(deque) > 0:
            print(deque.pop(0))
        else:
            print(-1)
    elif commend[0] == 'pop_back':
        if len(deque) > 0:
            print(deque.pop(-1))
        else:
            print(-1)
    elif commend[0] == 'size':
        print(len(deque))
    elif commend[0] == 'empty':
        if len(deque) == 0:
            print(1)
        else:
            print(0)
    elif commend[0] == 'front':
        if len(deque) > 0:
            print(deque[0])
        else:
            print(-1)
    elif commend[0] == 'back':
        if len(deque) > 0:
            print(deque[-1])
        else:
            print(-1)