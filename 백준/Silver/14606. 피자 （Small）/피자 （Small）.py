n = int(input())

dp = [0] * 12

dp[1] = 0
dp[2] = 1

for i in range(3, n + 1):
    div = i // 2
    dp[i] = (div * (i - div)) + dp[div] + dp[i - div]

print(dp[n])