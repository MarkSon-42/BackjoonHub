N = int(input())
points = []

for _ in range(N):
    x, y = map(int, input().split())
    points.append((x, y))

# x좌표가 증가하는 순으로, x좌표가 같으면 y좌표가 증가하는 순서로 정렬
points = sorted(points)

for point in points:
    print(point[0], point[1])