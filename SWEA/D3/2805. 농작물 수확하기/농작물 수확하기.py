t = int(input())

for tc in range(1, t + 1):
    n = int(input())
    grid = [list(map(int, input())) for _ in range(n)]
    revenue = 0

    # left, right
    left, right = n // 2, n // 2

    for i in range(n):
        for j in range(left, right + 1):
            revenue += grid[i][j]
        # 행의 인덱스가 중간 전까지는 좌, 우 간격 늘리고 중간 지나고 부터는 줄이기 : 인덱스 마름모 진행
        mid = n // 2
        if i < mid:
            left -= 1
            right += 1
        else:
            left += 1
            right -= 1

    print(f"#{tc} {revenue}")
