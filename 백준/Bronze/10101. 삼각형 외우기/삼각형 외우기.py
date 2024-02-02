ang_lst = []

for i in range(3):
    ang_lst.append(int(input()))

if sum(ang_lst) == 180:
    if ang_lst.count(60) == 3:
        print('Equilateral')
    elif ang_lst[0] == ang_lst[1] or ang_lst[0] == ang_lst[2] or ang_lst[1] == ang_lst[2]:
        print('Isosceles')
    else:
        print('Scalene')
else:
    print('Error')