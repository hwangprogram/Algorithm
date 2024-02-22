N, M = map(int, input().split())
word_lst = []
search_word = []
cnt = 0

for n in range(N):
    word_lst.append(input())

for m in range(M):
    search_word.append(input())

for m in range(M):
    if search_word[m] in word_lst:
        cnt += 1

print(cnt)