'''
백준 2628 종이자르기

문제 요약
직사각형 모양 종이가 주어진다.
이 종이를 가로 또는 세로로 자른다.
자를때는 종이를 끝까지 자른다. (도중에 멈추지 않는다)
0은 가로, 1은 세로이며
어디부터 자를 것인지가 주어진다.
'''
col, row = map(int, input().split())    # 종이의 열 개수 col, 행 개수 row

slices = int(input())    # 자를 횟수 slices

y_lst, x_lst = [], []     # 가로, 세로 자르는 위치 배열
y_can, x_can = [], []   # 넓이 구할 후보 배열
for _ in range(slices):
    direction, num = map(int, input().split())  # 자를 방향, 점선 번호 (행or열)

    if direction == 0:      # 가로라면?
        y_lst.append(num)
    else:                   # 세로라면?
        x_lst.append(num)

y_lst.sort()
x_lst.sort()

if len(x_lst) > 0:
    x_can.append(x_lst[0])
    for i in range(len(x_lst)-1):
        x_can.append(x_lst[i+1] - x_lst[i])
    x_can.append(col - x_lst[-1])
else:
    x_can.append(col)

if len(y_lst) > 0:
    y_can.append(y_lst[0])
    for i in range(len(y_lst)-1):
        y_can.append(y_lst[i+1] - y_lst[i])
    y_can.append(row - y_lst[-1])
else:   # 없다면
    y_can.append(row)

mx_mul = 0
for x in x_can:
    for y in y_can:
        mul = x*y
        mx_mul = max(mx_mul, mul)

print(mx_mul)