import sys

N = int(sys.stdin.readline())
stack = []

for _ in range(N):
    order = sys.stdin.readline().split()

    if order[0] == '1':
        stack.append(order[1])
    elif order[0] == '2':
        if len(stack) > 0:
            print(stack.pop())
        else:
            print(-1)
    elif order[0] == '3':
        print(len(stack))
    elif order[0] == '4':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    else:
        if len(stack) > 0:
            print(stack[-1])
        else:
            print(-1)