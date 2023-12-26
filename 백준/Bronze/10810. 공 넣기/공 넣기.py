n, m = map(int, input().split())

basket = [0] * (n + 1)

for _ in range(m):
    i, j, k = map(int, input().split())
    for i in range(i, j + 1):
        basket[i] = k

answer = basket[1:]

for i in range(n):
    print(answer[i], end=" ")
