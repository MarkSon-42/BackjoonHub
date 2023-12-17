import sys

input = sys.stdin.readline

n = int(input())

students = list(map(int, input().split()))

answer = 0

dp = [0] * (n + 1)

for i in range(n + 1):
    max_val = 0
    min_val = 10001

    for j in range(i, 0, -1):
        max_val = max(max_val, students[j - 1])
        min_val = min(min_val, students[j - 1])
        dp[i] = max(dp[i], max_val - min_val + dp[j - 1])

print(dp[n])
