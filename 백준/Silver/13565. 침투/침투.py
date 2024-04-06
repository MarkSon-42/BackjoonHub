from collections import deque
import sys

directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

M, N = map(int, sys.stdin.readline().split())
grid = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(M)]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()

        # If we reached the bottom row
        if x == M - 1:
            print('YES')
            exit(0)

        # Check all directions
        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if 0 <= nx < M and 0 <= ny < N and grid[nx][ny] == 0:
                grid[nx][ny] = 1
                queue.append((nx, ny))

for i in range(N):  # Change here
    if grid[0][i] == 0:
        bfs(0, i)

print('NO')