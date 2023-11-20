# 5 4

# 1 2
# 3 4
# 1 4
# 2 2

# 1 2 3 4 5

# 2 1 3 4 5
# 2 1 4 3 5
# 3 4 1 2 5
# 3 4 1 2 5


n, m = map(int, input().split())

buckets = [i for i in range(1, n + 1)]


for i in range(m):
    a, b = map(int, input().split())
    tmp = buckets[a - 1 : b]
    tmp.reverse()
    buckets[a - 1 : b] = tmp

for c in buckets:
    print(c, end=" ")
