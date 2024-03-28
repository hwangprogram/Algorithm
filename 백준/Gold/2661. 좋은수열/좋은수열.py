import sys
input = sys.stdin.readline

num = []
def make_num():
    global good, flag

    if flag:
        return

    # 가지치기: 인접한 같은수열 거르기
    if len(num) > 3:
        if judge(num):
            return

    # 기저조건: 길이가 N이상 되면 종료
    if len(num) == N:
        # 정답 처리: 최솟값
        # 좋은 수열 정수값으로 바꾸기
        good = int(''.join(num))
        flag = True
        return

    # 재귀조건: num에 수 포함 or 미포함
    # 1,2,3 만 사용
    for i in range(1, 4):
        # 그 전 수와 같은 값을 추가하지 않음(안좋은 수열이 됨)
        if len(num) > 0:
            if num[-1] != str(i):
                num.append(str(i))
                make_num()
                num.pop()
        else:
            num.append(str(i))
            make_num()
            num.pop()

# judge: 2~N//2개씩 슬라이싱하며 확인
def judge(number):
    rng = len(number)
    # 슬라이싱할 범위
    for i in range(2, rng//2+1):
        # 시작 위치(인덱스)
        for j in range(0, rng - (2*i) + 1):
            if number[j:j+i] == number[j+i:j+(2*i)]:
                return True
    else:
        return False


# N 길이의 수열
N = int(input().strip())

# 최소 좋은수열
good = 0
flag = False
make_num()
print(good)