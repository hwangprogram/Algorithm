T = 10

for tc in range(1, T + 1):
    str_len = int(input())      # 계산식의 길이
    formula = input()           # 계산식
    postfix = ''                # 후위 표기법으로 나타낸 계산식
    stack = []                  # 연산자 스택
    fx_stack = []               # 피연산자 스택

    # 연산자가 + 하나밖에 없기 때문에 스택에 2개이상 쌓이면 무조건 pop하고 후위표기 문자열에 추가
    for tk in formula:
        if tk == '+':
            stack.append(tk)
            if len(stack) > 1:
                postfix += tk
        else:
            postfix += tk
    postfix += stack[-1]
    
    # 숫자를 만나면 fx_stack에 append, +연산자를 만나면 스택 뒤의 숫자 두개를 plus
    for tk in postfix:
        if tk == '+':
            back = int(fx_stack.pop())
            front = int(fx_stack.pop())
            fx_stack.append(front + back)
        else:
            fx_stack.append(tk)

    print(f'#{tc} {fx_stack[-1]}')