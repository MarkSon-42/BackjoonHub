n = int(input())
s = sorted([list(map(int, input().split()))[::-1] for _ in range(n)])

ans = 0
t = 0
for i in range(n):
    if t > s[i][1]:
        continue
    ans += 1
    t = s[i][0]

print(ans)