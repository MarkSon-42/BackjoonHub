points = [list(map(int, input().split())) for _ in range(3)]

x_points = [point[0] for point in points]
y_points = [point[1] for point in points]

for x in x_points:
    if x_points.count(x) == 1:
        x4 = x
        break

for y in y_points:
    if y_points.count(y) == 1:
        y4 = y
        break

print(x4, y4)