import sys

N = int(sys.stdin.readline())

for num in range(N + 1):
    goal_num = 0
    goal_num += num
    num = str(num)

    for n in num:
        goal_num += int(n)

    if goal_num == N:
        print(num)
        break
else:
    print(0)