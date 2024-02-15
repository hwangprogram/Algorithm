import sys

T = int(sys.stdin.readline())

for _ in range(T):
    cmd = sys.stdin.readline().rstrip()  # 명령어를 문자열로 받음
    n = int(sys.stdin.readline().rstrip())  # 리스트의 길이를 받음
    lst = sys.stdin.readline().rstrip()  # 리스트를 문자열로 받음

    if lst != '[]':  # 리스트가 비어있지 않다면
        lst = list(map(int, lst[1:-1].split(',')))  # 리스트를 파싱하여 정수 리스트로 변환
    else:
        lst = []  # 빈 리스트인 경우

    # 명령어를 한 번에 처리
    reverse_flag = False
    start, end = 0, len(lst)
    for command in cmd:
        if command == 'R':
            reverse_flag = not reverse_flag
        else:  # 'P'
            if not lst:  # 리스트가 비어있으면
                print('error')
                break
            if reverse_flag:
                lst.pop()
            else:
                lst.pop(0)
    else:  # 에러가 발생하지 않았을 경우
        if reverse_flag:
            lst.reverse()
        print('[{}]'.format(','.join(map(str, lst))))