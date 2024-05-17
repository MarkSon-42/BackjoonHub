n = int(input())
dp = [0] + [float('inf')] * n

for i in range(1, int(n**0.5)+1):
    for j in range(i*i, n+1):
        dp[j] = min(dp[j], dp[j-i*i] + 1)

print(dp[n])