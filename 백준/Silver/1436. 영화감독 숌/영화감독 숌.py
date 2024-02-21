N = int(input())

cnt = 0         # 몇번째인지 세줄 카운트
result = 666    # 666부터 시작

while True:     # N번째 값이 나올 때 까지 반복
    if '666' in str(result):
        cnt += 1

    if cnt == N:
        break

    result += 1

print(result)