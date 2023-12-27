n = int(input())
roads = []
for i in range(n):
    a, b = map(int, input().split())
    roads.append((a, b))

most = sorted(roads, key=lambda x: x[1])

print(most[0][0], most[0][1])
