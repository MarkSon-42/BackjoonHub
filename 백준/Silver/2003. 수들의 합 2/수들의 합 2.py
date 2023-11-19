# m이 300,000,000
# n은 10,000

# 10,000 ^ 2 = 100,000,000

# time limit 0.5sec

# python이라면 two-pointer로 풀어야함.

import sys

input = sys.stdin.readline

n, m = map(int, input().split())
a = list(map(int, input().split()))

_sum = a[0]
left = 0
right = 1
cnt = 0

while True:
    if _sum < m:
        if right < n:
            _sum += a[right]
            right += 1
        else:
            break
    elif _sum == m:
        cnt += 1
        _sum -= a[left]
        left += 1
    else:
        _sum -= a[left]
        left += 1

print(cnt)