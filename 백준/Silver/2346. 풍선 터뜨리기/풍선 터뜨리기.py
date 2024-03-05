import sys
from collections import deque

N = int(input())

balloons = deque()
for n in range(1, N+1):
    balloons.append(n)

paper = deque(map(int, input().split()))

while paper:
    print(balloons.popleft(), end=' ')
    if paper[0] > 0:
        val = paper.popleft() - 1
    else:
        val = paper.popleft()
    balloons.rotate(-val)
    paper.rotate(-val)