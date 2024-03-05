import sys
input = sys.stdin.readline

T = int(input())

chat_set = set()
save = 0
for _ in range(T):
    chatting = input().rstrip()

    if chatting == 'ENTER':
        save += len(chat_set)
        chat_set = set()
    else:
        chat_set.add(chatting)

print(save + len(chat_set))