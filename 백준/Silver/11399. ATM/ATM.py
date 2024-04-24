N = int(input())
P = list(map(int, input().split()))

P.sort()

total = 0
for i in range(N):
    for j in range(i + 1):
        total += P[j]

print(total)