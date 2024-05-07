T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    lst = list(map(int, input().split()))
    answer = 0
    start = 0
    while start < N:
        idx_max = start
        for i in range(start + 1, N):
            if lst[idx_max] < lst[i]:
                idx_max = i
        for i in range(start, idx_max):
            answer += (lst[idx_max] - lst[i])
        start = idx_max + 1
    print(f'#{tc} {answer}')