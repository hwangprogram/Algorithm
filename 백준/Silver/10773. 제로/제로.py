K = int(input())
stack = []

for k in range(K):
    order = int(input())

    if order == 0:
        stack.pop()
    else:
        stack.append(order)

print(sum(stack))