def solve():
    dr = [(0, 1), (1, 0), (1, 1), (-1, 1)]
    for si in range(N):
        for sj in range(N):
            for di, dj in dr:
                cnt = 0
                for mul in range(5):
                    ni, nj = si + di * mul, sj + dj * mul
                    if 0 <= ni < N and 0 <= nj < N and grid[ni][nj] == 'o':
                        cnt += 1
                    else:
                        break
                if cnt == 5:
                    return 'YES'
    return 'NO'



T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    grid = [input() for _ in range(N)]

    answer = solve()

    print(f"#{tc} {answer}")