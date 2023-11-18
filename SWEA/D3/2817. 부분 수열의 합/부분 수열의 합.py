# 백트래킹

# 현재 방문 지역의 값을 더해준 뒤(temp) 다음을 호출 idx + 1

# 현재 방문 지역의 값을 더해주지 않고(sum_num) 다음을 호출 -> idx + 1


def solve(idx, sum_num):
    global cnt
    if idx >= n:
        return

    temp = sum_num + numlist[idx]
    if temp == k:
        cnt += 1

    solve(idx + 1, temp)

    solve(idx + 1, sum_num)


t = int(input())
for tc in range(1, t + 1):
    n, k = map(int, input().split())
    numlist = list(map(int, input().split()))
    cnt = 0
    solve(0, 0)
    print(f"#{tc} {cnt}")
