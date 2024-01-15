n = int(input())
num = str(input())
arr = list(num)
sum = 0

for i in range(len(arr)):
    sum += int(arr[i])

print(sum)