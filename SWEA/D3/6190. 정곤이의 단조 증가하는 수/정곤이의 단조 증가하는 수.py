T = int(input())

for tc in range(1, T+1):
    N = int(input())    # N개의 합칠 정수

    num_lst = list(map(int, input().split()))   # N개의 정수들
    mul_lst = []        # ixj한 것들의 리스트
    inc_lst = []        # 단조증가 리스트

    for i in range(N):
        for j in range(i+1, N):
            mul_lst.append(str(num_lst[i] * num_lst[j]))    # num리스트 내 숫자들의 곱을 전부 추가

    for num in mul_lst:
        cnt = 1

        if len(num) == 1:
            inc_lst.append(int(num))                  # 한자리수라면 단조증가 리스트에 추가

        for n in range(len(num) - 1):
            if int(num[n]) <= int(num[n+1]):     # 앞자리가 뒷자리보다 작거나 같으면
                cnt += 1        # 그 만큼 센다
            else:               # 앞자리가 더 크면 더이상 진행할 필요 x
                break

        if cnt == len(num):     # 쭉 오름차순이면
            inc_lst.append(int(num))  # 숫자를 단조증가리스트에 추가

    if inc_lst:     # 단조증가리스트에 값이 있다면
        print(f'#{tc} {max(inc_lst)}')  # 그 중 최대값 출력
    else:           # 없으면
        print(f'#{tc} -1')  # -1 출력
