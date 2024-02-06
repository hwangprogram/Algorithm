num_dict = {'ZRO': 0, 'ONE': 1, 'TWO': 2, 'THR': 3, 'FOR': 4, 'FIV': 5, 'SIX': 6, 'SVN': 7, 'EGT': 8, 'NIN': 9}

T = int(input())

for tc in range(1, T + 1):
    # 입력
    # 테스트케이스 넘버, 각 테스트케이스 길이
    T_N, T_len = input().split()
    T_len = int(T_len)
    # num 리스트
    num = list(input().split())

    # 논리
    # 각 단어별 숫자를 매칭해놓은 딕셔너리로 문자열 리스트를 정수 리스트로 변형한다.
    for i in range(T_len):
        num[i] = num_dict[num[i]]

    # 정수리스트로 변형된 리스트를 정렬한다.
    num.sort()

    # 정렬된 리스트를 다시 문자열로 바꿔 출력한다.
    # 딕셔너리의 키, 값을 서로 바꾼다
    ston_dict = {v:k for k, v in num_dict.items()}
    print(f'#{tc}')
    for i in num:
        print(ston_dict[i], end=' ')
    print()