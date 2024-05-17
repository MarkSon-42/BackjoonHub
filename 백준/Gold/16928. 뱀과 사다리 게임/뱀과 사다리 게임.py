from collections import deque

def bfs():
    q = deque()
    q.append((1, 0))
    visited = [0 for i in range(101)]
    visited[1] = 1

    while q:
        pos, cnt = q.popleft()
        if pos == 100:
            return cnt
        for i in range(1, 7):
            next_pos = pos + i
            if next_pos > 100:
                continue
            if next_pos in ladders:
                next_pos = ladders[next_pos]
            elif next_pos in snakes:
                next_pos = snakes[next_pos]
            if not visited[next_pos]:
                visited[next_pos] = 1
                q.append((next_pos, cnt + 1))

N, M = map(int, input().split())
ladders = {}
snakes = {}

for i in range(N):
    x, y = map(int, input().split())
    ladders[x] = y

for i in range(M):
    u, v = map(int, input().split())
    snakes[u] = v

print(bfs())