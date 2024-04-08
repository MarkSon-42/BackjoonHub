t = int(input())
dp = [[[0]*2 for _ in range(100)] for _ in range(101)]
dp[1][0][1] = 1
dp[1][0][0] = 1

for k in range(100):
    for n in range(2, 101):
        if k == 0:
            dp[n][k][1] = dp[n-1][k][0]
        else:
            dp[n][k][1] = dp[n-1][k][0] + dp[n-1][k-1][1]
        dp[n][k][0] = dp[n-1][k][0] + dp[n-1][k][1]

for _ in range(t):
    n, k = map(int, input().split())
    print(dp[n][k][0] + dp[n][k][1])