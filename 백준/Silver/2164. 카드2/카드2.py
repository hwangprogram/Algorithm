from collections import deque

N = int(input())

queue = deque()
for n in range(1, N+1):
    queue.append(n)

while len(queue) != 1:
    queue.popleft()
    queue.rotate(-1)

print(*queue)