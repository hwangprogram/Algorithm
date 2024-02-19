T = int(input())

for tc in range(1, T + 1):
    N = int(input())

    card = list(input().split())

    if N % 2 == 0:
        sep_lst1 = card[:N // 2]
        sep_lst2 = card[N // 2:]
    else:
        sep_lst1 = card[:N // 2 + 1]
        sep_lst2 = card[N // 2 + 1:]

    print(f'#{tc}', end=' ')

    for i in range(len(sep_lst1)):  # 둘 중 길이가 긴 리스트의 길이만큼
        print(sep_lst1.pop(0), end=' ')

        if sep_lst2:    # 리스트가 비어 있지 않다면
            print(sep_lst2.pop(0), end=' ')
    print()