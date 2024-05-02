answer = 0
coins = []
n, k = map(int, input().split())
for _ in range(n):
    coins.append(int(input()))

coins.reverse()

for coin in coins:
    if k >= coin:
        answer += k // coin
        k %= coin
        if k <= 0:
            break

print(answer)