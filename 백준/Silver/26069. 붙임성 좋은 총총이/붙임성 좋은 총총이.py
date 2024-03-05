N = int(input())

dance = {'ChongChong'}
cnt = 0
for _ in range(N):
    p1, p2 = input().split()

    if p1 in dance:
        dance.add(p2)
        
    if p2 in dance:
        dance.add(p1)

print(len(dance))