T = int(input())

for tc in range(1, T + 1):
    # 입력
    # 입력할 문자열 A, 그룹화된 문자열 B
    A, B = input().split()

    # A내부에 있는 B의 값을 카운트 (카운트 값 + B값들을 제거한 문자열의 길이가 답이 되기 때문)
    cnt = A.count(B)

    # B값의 길이 확인
    B_len = len(B)

    # B를 제거한 A의 길이
    remove_AtoB = len(A) - len(B) * cnt + cnt

    print(f'#{tc} {remove_AtoB}')
    