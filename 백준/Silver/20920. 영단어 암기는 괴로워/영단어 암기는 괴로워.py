'''
백준 20920 영단어 암기는 괴로워

여러 개의 단어 N개가 주어진다.
그 중 단어의 길이가 M 이상인 것들을 화은이는 단어장에 넣는다.
단어에는 우선순위가 있다.
1. 자주 나오는 단어일수록 앞에 배치한다.
2. 해당 단어의 길이가 길수록 앞에 배치한다.
3. 알파벳 사전 순으로 앞에 있는 단어일수록 앞에 배치한다.
'''
import sys
input = sys.stdin.readline

# N: 단어의 개수, M: 외울 단어의 길이 기준
N, M = map(int, input().split())

# 딕셔너리에 단어가 나온 횟수 저장
word_dict = dict()
for _ in range(N):
    word = input().rstrip()
    word_dict.setdefault(word, 1)
    word_dict[word] += 1

# 딕셔너리의 키 중에 길이가 M 이상인 것 고르기
item_lst = list(word_dict.items())
sorted_lst = []
for item in item_lst:
    if len(item[0]) >= M:
        sorted_lst.append(item)

# 1. 자주 나오는 단어 조건에 맞춰 정렬
# 2. 해당 단어의 길이가 길수록 앞에 배치
# 3. 알파벳 사전 순으로 앞에 있는 단어일수록 앞에 배치
# key lambda를 이용하여 구현
sorted_lst.sort(key=lambda x: (100000 - x[1], 10 - len(x[0]), x[0]))

for lst in sorted_lst:
    print(lst[0])