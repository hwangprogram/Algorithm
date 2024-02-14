# 1~n 까지의 수열
n = int(input())

ans = []
find = True

# 수열을 만들 stack
stack = []

# 1 ~ n까지의 숫자
num = 1

for _ in range(n):
    n = int(input())

    # 스택 쌓기
    while num <= n:
        stack.append(num)
        ans.append('+')
        num += 1

    # 스택 꺼내기
    if stack[-1] == n:
        stack.pop()
        ans.append('-')

    # 불가능한 경우
    else:
        find = False


# 출력
if not find:    # 불가능하다면
    print('NO')
else:
    for i in ans:   # 가능하다면
        print(i)