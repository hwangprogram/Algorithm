T = int(input())

for tc in range(1, T + 1):
    # 입력
    test_case = int(input())
    score = list(map(int, input().split()))

    # 로직
    # 각 값 카운트할 리스트 cnt_lst
    cnt_lst = []

    # 중복 제거한 리스트 no_dup_sc
    no_dup_sc = sorted(list(set(score)))

    # 중복없는 점수 리스트를 순회하며 점수들의 갯수 카운트
    for i in range(len(no_dup_sc)):
        cnt_lst.append(score.count(no_dup_sc[i]))

    if cnt_lst.count(max(cnt_lst)) > 1:
        cnt_lst.reverse()
        no_dup_sc.reverse()
        print(f'#{tc}', end=' ')
        print(no_dup_sc[cnt_lst.index(max(cnt_lst))])
    else:
        print(f'#{tc}', end=' ')
        print(no_dup_sc[cnt_lst.index(max(cnt_lst))])