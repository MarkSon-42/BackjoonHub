from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(x, y):
    q = deque([(x, y)])
    grid[x][y] = 1
    cnt = 1

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if nx < 0 or nx >= M or ny < 0 or ny >= N:
                continue

            if grid[nx][ny] == 0:
                q.append((nx, ny))
                grid[nx][ny] = 1
                cnt += 1

    return cnt

M, N, K = map(int, input().split())
grid = [[0] * N for _ in range(M)]
areas = []

for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(y1, y2):
        for j in range(x1, x2):
            grid[i][j] = 1

for i in range(M):
    for j in range(N):
        if grid[i][j] == 0:
            areas.append(bfs(i, j))

areas.sort()

print(len(areas))
for ar in areas:
    print(ar, end=' ')