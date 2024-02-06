import sys

N = int(sys.stdin.readline())
que = []

for tc in range(1, N + 1):
    commend = sys.stdin.readline().split()

    if commend[0] == 'push':
        que.append(commend[1])
    elif commend[0] == 'pop':
        if len(que) == 0:
            print(-1)
        else:
            print(que.pop(0))
    elif commend[0] == 'size':
        print(len(que))
    elif commend[0] == 'empty':
        if len(que) == 0:
            print(1)
        else:
            print(0)
    elif commend[0] == 'front':
        if len(que) == 0:
            print(-1)
        else:
            print(que[0])
    elif commend[0] == 'back':
        if len(que) == 0:
            print(-1)
        else:
            print(que[len(que) - 1])