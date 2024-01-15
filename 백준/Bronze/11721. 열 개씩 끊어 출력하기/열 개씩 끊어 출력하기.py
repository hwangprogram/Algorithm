N = str(input())

# 문자열의 길이가 10이상이라면 슬라이싱, 아니라면 그대로 출력
if len(N) >= 10:
    mx = len(N) // 10 # 문자열 길이의 십의 자리 숫자
    mt = len(N) % 10 # 문자열 길이의 일의 자리 숫자
    for i in range(1, mx + 1): # 문자열 슬라이싱을 위한 for문
        less = 10 * (i - 1)
        more = 10 * i
        print(N[less:more])
    print(N[mx * 10:])

else:
    print(N)