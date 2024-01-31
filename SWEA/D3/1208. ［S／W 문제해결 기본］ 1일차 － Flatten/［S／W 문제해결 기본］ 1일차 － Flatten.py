T = 10

for tc in range(1, T + 1):
    # 입력
    # 덤프(제일 큰값에서 제일 작은값으로 이동)하는 횟수
    dump = int(input())
    # 평탄화 할 토양의 리스트 soils
    soils = list(map(int, input().split()))

    # 로직
    # 가장 큰값에서 1을 뺀다, 가장 작은값에서 1을 더한다.
    # 위 과정을 dump번 만큼 반복한다.
    # 만약 dump번만큼 진행하기 전 평탄화가 완료되었다면 (높이차가 1 이하가 된다면)
    # 그 당시의 높이 차를 반환한다. (height)
    height = 0

    for i in range(dump):
        # 최대값의 위치 max_s
        max_s = soils.index(max(soils))
        # 최솟값의 위치 min_s
        min_s = soils.index(min(soils))
        soils[max_s] -= 1
        soils[min_s] += 1
        height = max(soils) - min(soils)
        if height <= 1:
            break

    # 출력
    print(f'#{tc} {height}')