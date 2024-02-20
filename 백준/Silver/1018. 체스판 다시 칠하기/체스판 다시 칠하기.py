'''
전략

슬라이싱을 적극 활용한다
8x8 체스판을 계속해서 만들고, 검사하고를 반복한다.
'''

N, M = map(int, input().split())

board = [input() for _ in range(N)]

ptn1 = ['WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW']  # 비교할 패턴1
ptn2 = ['BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB']  # 비교할 패턴2

min_v = 64

for i in range(N-7):
    chess = board[i:i + 8]      # 8x8 크기의 체스판
    for j in range(M-7):

        for h in range(8):
            chess[h] = board[i+h][j:j+8]

        min_dif = 0
        dif_ptn1 = dif_ptn2 = 0

        for k in range(8):      # 이 체스판에서 조건을 따져보고 다시 칠해야 할 칸의 수를 센다.
            for l in range(8):
                if chess[k][l] != ptn1[k][l]:
                    dif_ptn1 += 1

                if chess[k][l] != ptn2[k][l]:
                    dif_ptn2 += 1
        min_dif = min(dif_ptn1, dif_ptn2)
        min_v = min(min_dif, min_v)
print(min_v)