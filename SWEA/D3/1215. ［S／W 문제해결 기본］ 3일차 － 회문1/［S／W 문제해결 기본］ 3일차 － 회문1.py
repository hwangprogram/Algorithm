T = 10

for tc in range(1, T + 1):
    # 길이 N의 회문 판별
    N = int(input())
    # 알파벳들이 들어있는 2차원 배열
    word_lst = [list(input()) for _ in range(8)]

    # 로직
    # N // 2만큼 push하고, N // 2만큼 pop하는데
    # 이 때 스택의 맨 위 값과 들어오려는 값이 같으면 pop
    # 반복 이후 stack에 값이 없으면 회문
    # 회문 스택을 쌓음
    stack = []
    # 회문 카운드
    pal_cnt = 0
    # 얼마나 시행할 것인가?
    half = N // 2
    # 가로 배열을 순회하며 회문 판별
    for i in range(8):
        for j in range(8 - N + 1):
            stack = []
            for k in range(N):
                if N % 2 == 0:  # 짝수라면
                    if k < half:
                        stack.append(word_lst[i][j + k])
                    else:
                        if stack[-1] == word_lst[i][j + k]:
                            stack.pop()
                else:   # 홀수라면
                    if k < half:
                        stack.append(word_lst[i][j + k])
                    elif k > half:
                        if stack[-1] == word_lst[i][j + k]:
                            stack.pop()
            if len(stack) == 0:
                pal_cnt += 1

    # 세로 문자배열
    rev_word = [list(tp) for tp in zip(*word_lst)]

    for i in range(8):
        for j in range(8 - N + 1):
            stack = []
            for k in range(N):
                if N % 2 == 0:  # 짝수라면
                    if k < half:
                        stack.append(rev_word[i][j + k])
                    else:
                        if stack[-1] == rev_word[i][j + k]:
                            stack.pop()
                else:  # 홀수라면
                    if k < half:
                        stack.append(rev_word[i][j + k])
                    elif k > half:
                        if stack[-1] == rev_word[i][j + k]:
                            stack.pop()
            if len(stack) == 0:
                pal_cnt += 1

    print(f'#{tc} {pal_cnt}')