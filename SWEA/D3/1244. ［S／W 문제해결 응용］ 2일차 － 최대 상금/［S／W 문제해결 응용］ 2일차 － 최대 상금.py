T = int(input())

for tc in range(1, T+1):
    N, chance = input().split()
    N = list(N)
    chance = int(chance)

    his = set()

    mx_N = 0
    def change(k):
        global mx_N

        # 가지치기 : 같은 레벨에 같은 숫자가 있다면 가지치기
        if (k, int(''.join(N))) in his:
            return
        # 히스토리에 기록
        his.add((k, int(''.join(N))))
        # 기저조건 : 뒤집기 횟수 다 썼으면 리턴
        if k == 0:
            # 정답처리
            if int(''.join(N)) > mx_N:
                mx_N = int(''.join(N))
            return

        for i in range(len(N)):
            for j in range(i+1, len(N)):
                N[i], N[j] = N[j], N[i]     # 위치 바꾸기
                change(k-1)                 # 기회 1번 소요
                N[i], N[j] = N[j], N[i]     # 원상복구

    change(chance)
    print(f'#{tc} {mx_N}')