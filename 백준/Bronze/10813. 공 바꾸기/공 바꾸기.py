def ball_swap(a, b, arr):
    tmp = arr[a]
    arr[a] = arr[b]
    arr[b] = tmp


n, m = map(int, input().split())
balls = [i for i in range(1, n + 1)]
for _ in range(m):
    x, y = map(int, input().split())
    ball_swap(x - 1, y - 1, balls)

for i in range(n):
    print(balls[i], end=" ")
