import sys
sys.setrecursionlimit(10 ** 9)
N = int(sys.stdin.readline())
rel = [[] for i in range(N+1)]
dp = [[0, 0] for _ in range(N+1)]

for _ in range(N-1):
    a, b = map(int , sys.stdin.readline().split(" "))
    rel[a].append(b)
    rel[b].append(a)

visited = [0 for i in range(N+1)]
def dfs(start):
    global rel
    global visited
    visited[start] = 1
    if len(rel[start]) == 0:
        dp[start][1] = 1
        dp[start][0] = 0
    else:
        for i in rel[start]:
            if visited[i] == 0:
                dfs(i)
                dp[start][1] += min(dp[i][0] , dp[i][1])
                dp[start][0] += dp[i][1]
        dp[start][1] += 1

dfs(1)
print(min(dp[1][0], dp[1][1]))
