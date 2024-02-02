while True:
    l1, l2, l3 = map(int, input().split())

    if l1 == 0 and l2 == 0 and l3 == 0:
        break

    if max(l1, l2, l3) < l1 + l2 + l3 - max(l1, l2, l3):
        if l1 == l2 == l3:
            print('Equilateral')
        elif (l1 == l2) or (l2 == l3) or (l1 == l3):
            print('Isosceles')
        elif l1 != l2 != l3:
            print('Scalene ')
    else:
        print('Invalid')