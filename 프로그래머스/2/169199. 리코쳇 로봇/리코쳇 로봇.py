from collections import deque

def solution(board):
    n, m = len(board), len(board[0])
    dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]
    visited = [[-1]*m for _ in range(n)]
    queue = deque()

    for i in range(n):
        for j in range(m):
            if board[i][j] == 'R':
                start = (i, j)
            if board[i][j] == 'G':
                end = (i, j)

    queue.append((start[0], start[1], 0))
    
    visited[start[0]][start[1]] = 0

    while queue:
        x, y, cnt = queue.popleft()
        if (x, y) == end:
            return cnt
        for i in range(4):
            nx, ny = x, y
            while True:
                nx += dx[i]
                ny += dy[i]
                if nx < 0 or nx >= n or ny < 0 or ny >= m or board[nx][ny] == 'D':
                    nx -= dx[i]
                    ny -= dy[i]
                    break
            if visited[nx][ny] == -1 or visited[nx][ny] > cnt + 1:
                visited[nx][ny] = cnt + 1
                queue.append((nx, ny, cnt + 1))

    return -1