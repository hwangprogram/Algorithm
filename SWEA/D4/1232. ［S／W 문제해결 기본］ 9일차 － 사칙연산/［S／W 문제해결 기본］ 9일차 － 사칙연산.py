def inorder(i):
    if i == 0:
        return

    inorder(left[i])
    inorder(right[i])
    postfix.append(node[i])


T = 10

for tc in range(1, T+1):
    N = int(input())    # 정점의 개수 N

    node = [0]*(N+1)    # 노드의 값 배열
    left = [0]*(N+1)    # 왼쪽 자식 배열
    right = [0]*(N+1)   # 오른쪽 자식 배열
    postfix = []

    for n in range(N):
        info = input().split()
        if len(info) == 4:
            node[int(info[0])] = info[1]        # 연산자
            left[int(info[0])] = int(info[2])   # 왼쪽 자식
            right[int(info[0])] = int(info[3])  # 오른쪽 자식
        else:
            node[int(info[0])] = int(info[1])   # 피연산자

    inorder(1)

    stack = []      # 후위표현식의 계산을 위한 스택
    for ch in postfix:
        if type(ch) == int:     # 피연산자 : 스택에 추가
            stack.append(ch)
        elif ch == '*':         # 연산자 : 스택의 2개 값을 꺼내서 계산
            b = stack.pop()
            a = stack.pop()
            temp = a * b
            stack.append(temp)  # 계산한 값 다시 넣어줌
        elif ch == '/':         # 연산자 : 스택의 2개 값을 꺼내서 계산
            b = stack.pop()
            a = stack.pop()
            temp = a / b
            stack.append(temp)  # 계산한 값 다시 넣어줌
        elif ch == '+':         # 연산자 : 스택의 2개 값을 꺼내서 계산
            b = stack.pop()
            a = stack.pop()
            temp = a + b
            stack.append(temp)  # 계산한 값 다시 넣어줌
        elif ch == '-':         # 연산자 : 스택의 2개 값을 꺼내서 계산
            b = stack.pop()
            a = stack.pop()
            temp = a - b
            stack.append(temp)  # 계산한 값 다시 넣어줌

    result = stack.pop()
    print(f'#{tc} {int(result)}')