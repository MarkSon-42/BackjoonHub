from collections import deque

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
dist = [[-1]*m for _ in range(n)]
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

queue = deque()
for i in range(n):
    for j in range(m):
        if grid[i][j] == 2:
            queue.append((i, j))
            dist[i][j] = 0

while queue:
    x, y = queue.popleft()
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] != 0 and dist[nx][ny] == -1:
            dist[nx][ny] = dist[x][y] + 1
            queue.append((nx, ny))

for i in range(n):
    for j in range(m):
        if grid[i][j] == 0:
            print(0, end=' ')
        else:
            print(dist[i][j], end=' ')
    print()