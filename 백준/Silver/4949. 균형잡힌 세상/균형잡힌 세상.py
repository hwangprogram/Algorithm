while True:
    sentence = input()

    s = ''

    if sentence == '.':
        break

    for sen in sentence:
        if sen not in '()[]':
            continue
        else:
            s += sen

    for _ in range(len(s)//2+1):
        s = s.replace('()', '')
        s = s.replace('[]', '')

    if len(s):
        print('no')
    else:
        print('yes')