from collections import deque

N = int(input())

# 큐
N_lst = deque(map(int, input().split()))
stack = deque()

i = 1
while N_lst:
    stack.append(N_lst.popleft())
    while len(stack) > 0 and stack[-1] == i:
        stack.pop()
        i += 1

if len(stack) == 0:
    print('Nice')
else:
    print('Sad')