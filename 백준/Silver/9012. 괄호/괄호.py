T = int(input())

for tc in range(1, T + 1):
    vps = input()

    stack = []
    ans = ''
    in_middle = False

    for i in vps:
        if i == '(':
            stack.append(i)
        else:
            try:
                stack.pop()
            except:
                in_middle = True

    if len(stack) == 0 and in_middle == False:
        ans = 'YES'
    else:
        ans = 'NO'
    print(ans)