import sys
from collections import deque

def bfs(start, goal, board, visited, l, r, c):
    dz = (1, -1, 0, 0, 0, 0)
    dx = (0, 0, 1, -1, 0, 0)
    dy = (0, 0, 0, 0, 1, -1)
    directions = list(zip(dz, dx, dy))

    q = deque([(*start, 0)])

    while q:
        z, x, y, d = q.popleft()
        if (z, x, y) == goal:
            return f'Escaped in {d} minute(s).'

        for dz, dx, dy in directions:
            nz, nx, ny = z + dz, x + dx, y + dy
            if 0 <= nz < l and 0 <= nx < r and 0 <= ny < c and not visited[nz][nx][ny] and board[nz][nx][ny] in {'.', 'E'}:
                q.append((nz, nx, ny, d + 1))
                visited[nz][nx][ny] = True

    return 'Trapped!'

while True:
    l, r, c = map(int, sys.stdin.readline().split())
    if l == r == c == 0:
        break

    board = []
    visited = [[[False] * c for _ in range(r)] for _ in range(l)]
    for _ in range(l):
        board.append([list(sys.stdin.readline().strip()) for _ in range(r)])
        sys.stdin.readline()

    start = goal = None
    for i in range(l):
        for j in range(r):
            for k in range(c):
                if board[i][j][k] == 'S':
                    start = (i, j, k)
                    visited[i][j][k] = True
                elif board[i][j][k] == 'E':
                    goal = (i, j, k)

    print(bfs(start, goal, board, visited, l, r, c))