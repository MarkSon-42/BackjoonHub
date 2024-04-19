import sys

# Counter Clockwise 함수
# 세 점이 반시계 방향으로 위치하는지 확인
def counter_clockwise(x1, y1, x2, y2, x3, y3):
    return x1*y2 + x2*y3 + x3*y1 - x2*y1 - x3*y2 - x1*y3

# 입력 받기
input = sys.stdin.readline
point1_x, point1_y = map(int, input().split())
point2_x, point2_y = map(int, input().split())
point3_x, point3_y = map(int, input().split())

# 세 점의 위치 판별
result = counter_clockwise(point1_x, point1_y, point2_x, point2_y, point3_x, point3_y)

# 결과 출력
if result > 0:
    print(1)
elif result < 0:
    print(-1)
else:
    print(0)