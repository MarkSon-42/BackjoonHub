t = 10
for tc in range(1, t + 1):
    n = int(input())
    lst = list(map(int, input().split()))

    for _ in range(n):
        lst.sort()
        lst[0] += 1
        lst[-1] -= 1
    answer = max(lst) - min(lst)
    print(f"#{tc} {answer}")