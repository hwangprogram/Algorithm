score_dict = {'A+': 4.5, 'A0': 4.0, 'B+': 3.5, 'B0': 3.0, 'C+': 2.5, 'C0': 2.0, 'D+': 1.5, 'D0': 1.0, 'F': 0.0}
score_lst = []
sum_sc = sum_per = 0

for i in range(20):
    subject, per, score = list(map(str, input().split()))
    per = float(per)

    if score == 'P':
        continue
    else:
        sum_per += per
        sum_sc += per * score_dict[score]

ans = sum_sc / sum_per

print(ans)