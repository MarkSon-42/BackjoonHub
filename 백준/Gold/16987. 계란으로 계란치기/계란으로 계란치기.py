# 완탐 dfs같은데 은근 까다로운 구현을 아무리 해도 안됨 100라인 넘어감

# dfs + 백트래킹 문제였음..ㅜㅜㅜㅜ

def dfs(n, cnt):
    global ans
    if ans >= (cnt + (N - n) * 2):
        return

    if n == N: 
        ans = max(ans, cnt)
        return

    if arr[n][0] <= 0: 
        dfs(n + 1, cnt)
    else: 
        flag = False  
        for j in range(N):
            if n == j or arr[j][0] <= 0:
                continue
            flag = True
            arr[n][0] -= arr[j][1]
            arr[j][0] -= arr[n][1]
            dfs(n + 1, cnt + int(arr[n][0] <= 0) + int(arr[j][0] <= 0))
            arr[n][0] += arr[j][1]
            arr[j][0] += arr[n][1]
        if not flag:
            dfs(n + 1, cnt)


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

ans = 0
dfs(0, 0)
print(ans)