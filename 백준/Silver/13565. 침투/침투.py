from collections import deque
import sys

# Define directions
directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

# Read input
N, M = map(int, sys.stdin.readline().split())
grid = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(N)]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()

        # If we reached the bottom row
        if x == N - 1:
            print('YES')
            exit(0)

        # Check all directions
        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            # If the new position is within the grid and is a white cell
            if 0 <= nx < N and 0 <= ny < M and grid[nx][ny] == 0:
                # Mark the cell as visited
                grid[nx][ny] = 1
                # Add the new position to the queue
                queue.append((nx, ny))

for i in range(M):
    if grid[0][i] == 0:
        bfs(0, i)

print('NO')