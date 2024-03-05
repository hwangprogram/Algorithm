import sys
from collections import deque

input = sys.stdin.readline()

N, K = map(int, input.split())

queue = deque()
for n in range(1, N+1):
    queue.append(n)

yoseputh = []
while queue:
    queue.rotate(-(K-1))
    yoseputh.append(queue.popleft())

ans = str(yoseputh)
ans = ans.replace('[', '<')
ans = ans.replace(']', '>')

print(ans)