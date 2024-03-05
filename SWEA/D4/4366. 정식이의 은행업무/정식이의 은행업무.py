T = int(input())

for tc in range(1, T+1):
    binary = input()
    trit = input()

    bin_lst, tr_lst = [], []
    for i in range(len(binary)):
        bin_lst.append(binary[:i] + str((int(binary[i]) + 1) % 2) + binary[i+1:])

    for i in range(len(trit)):
        for j in range(1, 3):
            tr_lst.append(trit[:i] + str((int(trit[i]) + j) % 3) + trit[i+1:])

    b_num_lst, t_num_lst = [], []
    # 이진수 -> 십진수
    for b in bin_lst:
        sum_b = 0

        for i in range(len(b) - 1, -1, -1):
            sum_b += (2 ** i) * int(b[len(b)-(i+1)])

        b_num_lst.append(sum_b)

    # 삼진수 -> 십진수
    for t in tr_lst:
        sum_t = 0

        for i in range(len(t) - 1, -1, -1):
            sum_t += (3 ** i) * int(t[len(t) - (i + 1)])

        t_num_lst.append(sum_t)

    print(f'#{tc}', end=' ')
    print(*set.intersection(set(b_num_lst), set(t_num_lst)))