T = 10

for tc in range(1, T+1):
    test_case = int(input())

    pw = list(map(int, input().split()))   # 비밀번호가 될 배열
    N = [1,2,3,4,5]

    while True:       # pw의 마지막 인덱스가 0이 될때까지
        if pw[-1] == 0:
            break

        for n in N:
            t = pw.pop(0)    # pw의 맨앞 값을 pop
            if (t-n) <= 0:    # t-n값이 0보다 작거나 같게 된다면,
                pw.append(0)
                break
            else:
                pw.append(t-n)

    print(f'#{test_case}', end=' ')
    for i in pw:
        print(i, end=' ')
    print()