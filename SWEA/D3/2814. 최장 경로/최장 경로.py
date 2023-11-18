def dfs(i, cnt):
    global max_vertex

    for j in range(1, n + 1):
        if not visited[j] and grid[i][j]:
            visited[j] = 1
            dfs(j, cnt + 1)
            visited[j] = 0
    else:
        if cnt > max_vertex:
            max_vertex = cnt


t = int(input())
for tc in range(1, t + 1):
    n, m = map(int, input().split())
    grid = [[0] * (n + 1) for _ in range(n + 1)]
    visited = [0] * (n + 1)
    max_vertex = 0
    for _ in range(m):
        x, y = map(int, input().split())
        grid[x][y] = 1
        grid[y][x] = 1
    for i in range(1, n + 1):
        visited[i] = 1
        dfs(i, 1)
        visited[i] = 0
    print(f"#{tc} {max_vertex}")
