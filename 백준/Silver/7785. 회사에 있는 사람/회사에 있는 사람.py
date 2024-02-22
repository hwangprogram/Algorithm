import sys

N = int(sys.stdin.readline())

in_company_lst = []

for n in range(N):
    name, status = sys.stdin.readline().split()

    if status == 'enter':
        in_company_lst.append(name)
    elif status == 'leave':
        in_company_lst.remove(name)

in_company_lst = sorted(in_company_lst, reverse=True)

for ppl in in_company_lst:
    print(ppl)