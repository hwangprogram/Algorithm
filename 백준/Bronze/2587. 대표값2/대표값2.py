arr = []

for i in range(5):
    arr.append(int(input()))

arr.sort()
avg = sum(arr) / len(arr)

print(int(avg))
print(arr[2])