n = int(input())
lists = sorted([list(map(int, input().split())) for _ in range(n)])
dp = [1]*n

for i in range(1, n):
    dp[i] = max([dp[i]] + [dp[j]+1 for j in range(i) if lists[j][1] < lists[i][1]])

print(n-max(dp))