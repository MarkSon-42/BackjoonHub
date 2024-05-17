from collections import deque
import sys


dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
def bfs(x, y):
    cnt = 0
    q = deque()
    q.append((x, y))

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and g[nx][ny] == 'O':
                g[nx][ny] = 'X'
                q.append((nx, ny))
            if 0 <= nx < N and 0 <= ny < M and g[nx][ny] == 'P':
                g[nx][ny] = 'X'
                q.append((nx, ny))
                cnt += 1

    if cnt != 0:
        print(cnt)
    else:
        print('TT')



N, M = map(int, input().split())

g = [list(map(str, input().rstrip())) for _ in range(N)]

for i in range(N):
    for j in range(M):
        if g[i][j] == 'I':
            bfs(i, j)