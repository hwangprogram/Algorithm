# 한수의 현재 위치 x, y, 직사각형: 0,0 부터 w, h까지.
x, y, w, h = map(int, input().split())

# 0,0과 w,h 중 가까운 곳으로 이동, 이동한 거리를 반환
# 거리의 최솟값
min_dis = min(x, y, w - x, h - y)

print(min_dis)