code_dict = {'0001101': '0',
        '0011001': '1',
        '0010011': '2',
        '0111101': '3',
        '0100011': '4',
        '0110001': '5',
        '0101111': '6',
        '0111011': '7',
        '0110111': '8',
        '0001011': '9'}

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())

    pw = [input() for _ in range(N)]

    pw_to_code = ''
    real_pw = None
    verify = 0
    ans = 0

    for i in range(N-1, -1, -1):
        for j in range(M-1, -1, -1):
            if pw[i][j] == '1':
                for k in range(8):
                    real_pw = pw[i][j-55:j+1]

                break

    for i in range(0, len(real_pw), 7):
        pw_to_code += code_dict[real_pw[i:i+7]]

    for i in range(len(pw_to_code)):
        if i % 2 == 0:
            verify += 3 * int(pw_to_code[i])
        else:
            verify += int(pw_to_code[i])

    if verify % 10 == 0:
        pw_to_code = map(int, pw_to_code)
        ans = sum(pw_to_code)
    else:
        ans = 0

    print(f'#{tc} {ans}')