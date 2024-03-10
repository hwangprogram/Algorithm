'''
백준 2447 별찍기 10
'''
def star(n):
    # 기저조건: n이 1이 되었을 때 *을 리턴
    if n == 1:
        return ['*']

    stars = star(n//3)  # *
    L = []

    for st in stars:
        L.append(st*3)
    for st in stars:
        L.append(st+' '*(n//3)+st)
    for st in stars:
        L.append(st*3)

    return L    # return 한 값이 다시 stars에 들어가고 계속해서 반복


N = int(input())

print('\n'.join(star(N)))