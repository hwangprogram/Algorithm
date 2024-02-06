import sys

N = int(sys.stdin.readline())
word_lst = []

for _ in range(1, N + 1):
    word_lst.append(sys.stdin.readline())

word_lst = list(set(word_lst))

for i in range(len(word_lst)):
    word_lst[i] = word_lst[i].replace('\n', '')

len_word_lst = [0] * len(word_lst)

for i in range(len(word_lst)):
    len_word_lst[i] = [len(word_lst[i]), word_lst[i]]

len_word_lst.sort()

for i in len_word_lst:
    print(i[1])