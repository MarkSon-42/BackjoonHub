for tc in range(1, 11):
    N = int(input())
    grid = [list(map(int, input().split())) for _ in range(100)]
    cnt = 0
    for j in range(100):
        flag = 0
        for i in range(100):
            if grid[i][j] == 1:
                flag = 1
            if grid[i][j] == 2 and flag == 1:
                flag = 0
                cnt += 1

    print(f'#{tc} {cnt}')