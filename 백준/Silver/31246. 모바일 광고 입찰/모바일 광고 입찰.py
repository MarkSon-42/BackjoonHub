N, K = map(int, input().split())
v = []

for _ in range(N):
    a, b = map(int, input().split())
    v.append(b - a)

v.sort()

print(max(0, v[K - 1]))