def kantoer(a, n):
    '''
    :param a: 시작점
    :param n: div값
    '''
    # 기저조건: n 이 1이 될때 (길이가 1인 선들만 남았을 때)
    if n == 1:
        return

    for i in range(a+n//3, a+2*(n//3)):
        st[i] = ' '
    # 실행
    kantoer(a, n//3)
    kantoer(a+2*(n//3), n//3)


while True:
    try:
        N = int(input())
        st = ['-'] * (3 ** N)
        kantoer(0, 3 ** N)
        print(''.join(st))
    except:
        break