for _ in range(10):
    tc = int(input())

    arr = [list(map(int, input().split())) for _ in range(100)]

    # 가로줄 합
    max_h = 0
    for i in range(100):
        sum_val = 0
        for j in range(100):
            sum_val += arr[i][j]
        if sum_val > max_h:
            max_h = sum_val

    # 세로줄 합
    max_v = 0
    for j in range(100):
        sum_val = 0
        for i in range(100):
            sum_val += arr[i][j]
        if sum_val > max_v:
            max_v = sum_val

    max_d = 0
    sum1, sum2 = 0, 0
    for i in range(100):
        
        sum1 += arr[i][i]
        sum2 += arr[i][99-i]
        
    max_d = max(sum1, sum2)
    

    print(f"#{tc} {max(max_h, max_v, max_d)}")
    