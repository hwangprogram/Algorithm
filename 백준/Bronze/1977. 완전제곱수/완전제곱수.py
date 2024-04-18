M = int(input())
N = int(input())
mul_nums = []

i = 1
while (i**2) <= N:
    if M <= (i**2) <= N:
        mul_nums.append(i**2)
    i += 1

if mul_nums:
    print(sum(mul_nums))
    print(mul_nums[0])
else:
    print(-1)