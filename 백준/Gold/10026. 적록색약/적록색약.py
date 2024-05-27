from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(x, y, grid, visited):
    color = grid[x][y]
    queue = deque([(x, y)])
    visited[x][y] = True

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue

            if grid[nx][ny] == color and not visited[nx][ny]:
                queue.append((nx, ny))
                visited[nx][ny] = True

N = int(input())
grid1 = [list(input()) for _ in range(N)]
grid2 = [['']*N for _ in range(N)]
visited1 = [[False]*N for _ in range(N)]
visited2 = [[False]*N for _ in range(N)]

for i in range(N):
    for j in range(N):
        if grid1[i][j] == 'G':
            grid2[i][j] = 'R'
        else:
            grid2[i][j] = grid1[i][j]

count1 = count2 = 0

for i in range(N):
    for j in range(N):
        if not visited1[i][j]:
            bfs(i, j, grid1, visited1)
            count1 += 1
        if not visited2[i][j]:
            bfs(i, j, grid2, visited2)
            count2 += 1

print(count1, count2)