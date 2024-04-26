import sys
from collections import deque

a, b, n, m = map(int,input().split())
visited = [False] * 100001
q = deque()
steps = 0

def bfs(n, steps):
    q.append((n, steps))
    while q:
        x, steps = q.popleft()
        for i in (x+a, x+b, x*a, x*b, x-a, x-b, x+1, x-1):
            if i == m:
                print(steps + 1)
                sys.exit(0)
            if 0 <= i < 100001 and not visited[i]:
                visited[i] = True
                q.append((i, steps + 1))

bfs(n, steps)