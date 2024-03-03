'''
백준 1244 스위치 켜고 끄기

문제 요약
1부터 N까지 있는 스위치가 주어진다.
이후, 학생의 인원수가 나오고, 성별과 받은 숫자가 주어진다.
남학생이라면 자기가 받은 배수 스위치의 상태를 바꾼다.
여학생이라면 자기가 받은 수와 같은 번호가 붙은 스위치를 중심으로 좌우가 대칭이면서
가장 많은 스위치를 포함하는 구간을 찾아서 그 구간에 속한 스위치의 상태를 모두 바꾼다.
'''

N = int(input())    # 스위치 갯수 N
switchs = list(map(int, input().split()))   # 스위치

ppls = int(input())  # 학생 수 num
for _ in range(ppls):
    gender, num = map(int, input().split())     # 성별, 받은 숫자

    if gender == 1:     # 남학생이라면: 받은 번호의 배수 스위치를 변경
        for n in range(num-1, N, num):
            switchs[n] = (switchs[n] + 1) % 2
    elif gender == 2:   # 여학생이라면: 받은 번호에서부터 양쪽으로 퍼져나가며 대칭인 구간을 찾아 그 구간을 변경
        num -= 1        # 인덱싱 편의성을 위해
        for i in range(N):
            if num - i >= 0 and num + i < N:    # 범위 내에 있다면
                if switchs[num - i] == switchs[num + i]:    # 양쪽이 대칭이라면
                    # 각 인덱스의 값들 변경
                    switchs[num - i], switchs[num + i] = (switchs[num - i] + 1) % 2, (switchs[num + i] + 1) % 2
                else:       # 아니라면
                    break   # 더이상 진행할 필요 x
            else:           # 범위 밖이라면
                break

if len(switchs) <= 20:      # 스위치가 20개 이하라면
    print(*switchs)
else:                       # 아니라면 (20개씩 끊어서 프린트)
    for n in range(0, N, 20):
        print(*switchs[n:n+20])