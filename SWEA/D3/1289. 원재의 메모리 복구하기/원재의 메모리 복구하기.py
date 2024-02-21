# 원재의 메모리 복구하기

T = int(input())

for tc in range(1, T+1):
    memory = input()

    defalt = '0' * len(memory)
    cnt = 0

    for i in range(len(memory)):
        if defalt[i] != memory[i]:
            if memory[i] == '1':
                defalt = defalt[:i] + '1' * len(defalt[i:])
                cnt += 1
            else:
                defalt = defalt[:i] + '0' * len(defalt[i:])
                cnt += 1

    print(f'#{tc} {cnt}')
