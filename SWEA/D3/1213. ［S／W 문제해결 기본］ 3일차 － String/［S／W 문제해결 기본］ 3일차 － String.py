T = 10

for tc in range(1, T + 1):
    # 입력
    # 각 테스트케이스 숫자
    test_case = int(input())
    # 찾아야 하는 패턴 값
    ptn = input()
    # 패턴을 찾을 문자
    txt = input()

    # 로직
    print(f'#{tc} {txt.count(ptn)}')
