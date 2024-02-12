T = int(input())

for tc in range(1, T+1):
    # 쇠막대기 수열 입력
    steel = input()

    steel = steel.replace('()', 'r')

    # 쇠막대기 or 레이저 값을 쌓을 스택
    stack = ''

    # 레이저를 세어줄 카운트 lazer
    lazer = 0

    # 쇠막대기(잘리기 전) 의 갯수
    og_bar = 0

    # 쇄막대기 갯수 bars
    bars = 0

    for i in range(len(steel)):
        # ( 라면 스택에 push
        if steel[i] == '(':
            stack += '('
        elif steel[i] == 'r':
            stack += 'r'
        # ) 를 만나게 되면 stack의 마지막에 있는 ( 과 ) 사이에
        # 몇개의 r이 있는지 세고, bars에 r + 1을 plus 함
        elif steel[i] == ')':
            cnt = stack[stack.rindex('('):].count('r')
            stack = stack[:stack.rindex('(')] + stack[stack.rindex('(') + 1:]
            bars += cnt + 1

    print(f'#{tc} {bars}')