# Eng = list(map(chr, range(65,90+1)))
# num = list(range(10,35+1))

#만약 입력 받은 알파벳이 Eng 안에 있다면 숫자로 바꾸고 -55, 만약 0~9까지 입력 받았다면 그대로 출력

N, B= input().split(" ")
N = ''.join(reversed(N))
B = int(B)

number = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# def jinbup(num):
#     result = 0
#     global N
#
#     for i in N:
#         if i in Eng:
#             result = ord(i)-55
#         elif int(i) in range(1,10):
#             result = int(i)
#         elif int(i) == 0:
#             continue
#     return result

total = 0

for i in range(len(N)-1,-1,-1):
    # num = jinbup(N[-i])
    sum = (B ** i) * number.index(N[i])
    total += sum

print(total)