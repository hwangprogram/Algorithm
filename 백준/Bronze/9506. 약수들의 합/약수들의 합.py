while True:
    # 입력
    # 완전수인지 아닌지 판단할 n
    n = int(input())

    # 로직
    # n에 -1의 입력이 들어오면 break
    if n == -1:
        break

    # 약수들을 추가해줄 리스트 sub_num_lst
    sub_num_lst = []

    # 전체 약수 구해주기
    for i in range(1, n + 1):
        if n % i == 0:
            # n을 걸러줘야 함
            if i != n:
                sub_num_lst.append(i)


    # 완전수인가?
    if sum(sub_num_lst) == n:

        # 출력
        # 출력 형식에 맞춰 출력
        print(n, '=', end=' ')
        for i in sub_num_lst:
            print(i, end=' ')
            if sub_num_lst.index(i) == len(sub_num_lst) - 1:
                pass
            else:
                print('+', end=' ')
    # 아닌가?
    else:
        print(f'{n} is NOT perfect.')