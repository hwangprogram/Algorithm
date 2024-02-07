T = 10

for tc in range(1, T + 1):
    # 입력
    # 연속된 문자
    ln, pw = input().split()

    # 로직
    # 연속된 값들을 지우며 쌓을 스택 문자열
    stack_str = ''

    # 문자를 순회하며 스택문자열에 추가
    for i in pw:
        # i를 스택 문자열에 추가
        stack_str += i
        # 스택 문자열의 끝 ~ 앞으로 2개까지의 값이 i를 두번 곱한것과 같다면
        if stack_str[-1:-3:-1] == i * 2:
            # 스택문자열을 그 두개를 제외한 문자열로 변경한다.
            stack_str = stack_str[0:-2]

    # 출력
    print(f'#{tc} {stack_str}')
