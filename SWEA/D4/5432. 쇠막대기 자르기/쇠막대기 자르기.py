'''
SWEA 쇠막대기 자르기

문제 요약:
()(((()())(())()))(())
이런식으로 주어졌을 때, () -> 바로 열고 닫긴 소괄호 : 레이저
그 외의 것들은 쇠막대기이다.
레이저로 절단한 후의 쇠막대기 수를 구하라

전략:
1. ()를 l로 바꿔준다 (lazer)
2. ( 이 나올때마다 stack에 쌓아주고, 'l'이 나올때 마다 카운트 해준 다음, )가 나오면 (을
pop해주면서 레이저카운트 + 1 만큼을 합에 더해줌
'''
T = int(input().rstrip())

for tc in range(1, T+1):
    steel = input().rstrip()

    steel = steel.replace('()', 'l')    # ()를 l로 바꿔준다.

    stack = []
    lazer_cnt = 0
    sm = 0
    '''
    lazer_cnt를 사용
    lazer_cnt는 스택에 쌓여있는 (과 )사이의 레이저 값
    '''
    cnt = 0
    for s in steel:
        if s == '(':    # (을 만나면 스택에 append하고, 얼마나 쌓였는지 체크함
            sm += 1
            stack.append(s)
        elif s == 'l':  # l을 만나면 자름 (자를 때 마다 현재 스택에 쌓인 괄호 수만큼 더해줌(등분)
            cnt = len(stack)
            sm += cnt
        elif s == ')':
            stack.pop()

    print(f'#{tc} {sm}')