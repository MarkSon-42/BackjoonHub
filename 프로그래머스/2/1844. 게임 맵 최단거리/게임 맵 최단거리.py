from collections import deque

def solution(maps):
    n, m = len(maps), len(maps[0])
    q = deque()
    q.append((0, 0))
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    while q:
        y, x = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < m and 0 <= ny < n and maps[ny][nx] == 1:
                maps[ny][nx] = maps[y][x] + 1
                q.append((ny, nx))
    
    return maps[n-1][m-1] if maps[n-1][m-1] > 1 else -1