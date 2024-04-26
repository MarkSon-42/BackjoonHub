N, M = map(int, input().split())

def dfs(start, depth, result):
    if depth == M:
        print(' '.join(map(str, result)))
        return
    for i in range(start, N+1):
        dfs(i, depth+1, result+[i])

dfs(1, 0, [])