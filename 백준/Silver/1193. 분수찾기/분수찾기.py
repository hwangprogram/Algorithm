X = int(input())
num = stage = 1

while num + stage <= X:
    num += stage
    stage += 1

pos = X - num
m = c = 0

if stage % 2 == 0:
    c = X - num + 1
    m = stage - X + num
elif stage % 2 == 1:
    m = X - num + 1
    c = stage - X + num

print(f'{c}/{m}')