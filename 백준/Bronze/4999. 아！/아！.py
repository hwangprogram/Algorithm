pat_a = 0
doc_a = 0

pat = input()
doc = input()

for p in pat:
    if p == 'a':
        pat_a += 1

for d in doc:
    if d == 'a':
        doc_a += 1

if pat_a >= doc_a:
    print('go')
else:
    print('no')