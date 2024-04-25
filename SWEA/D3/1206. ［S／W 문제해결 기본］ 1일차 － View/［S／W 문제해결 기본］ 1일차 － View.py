for tc in range(1, 11):
    answer = 0
    n = int(input())
    b = list(map(int, input().split()))
    for i in range(2, n - 2):
        if max(b[i-2], b[i-1], b[i], b[i+1], b[i+2]) == b[i]:
            answer += b[i] - max(b[i-2], b[i-1], b[i+1], b[i+2])

    print(f"#{tc} {answer}")