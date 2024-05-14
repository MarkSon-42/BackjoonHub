N, M, B = map(int, input().split())
blocks = [list(map(int, input().split())) for _ in range(N)]

min_height = min(min(row) for row in blocks)
max_height = max(max(row) for row in blocks)

min_time = float('inf')
optimal_height = -1

for height in range(min_height, max_height + 1):
    plus = 0
    minus = 0
    for i in range(N):
        for j in range(M):
            if blocks[i][j] < height:
                plus += height - blocks[i][j]
            else:
                minus += blocks[i][j] - height

    if minus + B >= plus:
        time = plus + 2 * minus
        if time <= min_time:
            min_time = time
            optimal_height = height

print(min_time, optimal_height)