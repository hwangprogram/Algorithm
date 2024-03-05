import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
A = deque(map(int, input().split()))
B = deque(map(int, input().split()))

queue = deque()
stack = deque()
for n in range(N):
    if A[n] == 0:   # 큐라면
        queue.append(B[n])
    else:           # 스택이라면
        stack.append(B[n])

M = int(input())
C = deque(map(int, input().split()))

for c in C:
    queue.appendleft(c)
    print(queue.pop(), end=' ')