import sys
from collections import deque


def bfs(g, s, v):
    q = deque()
    q.append(s)
    v[s] = True

    while q:
        current_node = q.popleft()
        for neighbor in g[current_node]:
            if not v[neighbor]:
                q.append(neighbor)
                v[neighbor] = True

n, m = map(int, input().split())
g = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)

c = 0
v = [False] * (n + 1)

for i in range(1, n + 1):
    if not v[i]:
        bfs(g, i, v)
        c += 1

print(c)