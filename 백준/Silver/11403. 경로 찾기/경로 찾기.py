# 경로에 관한 문제가 나왔을 때 bfs 기본 솔루션

# .. 이게 가장 빠른 풀이라고 하는데 제법 실행시간이 길다

from collections import deque

N = int(input())

g = [list(map(int, input().split())) for _ in range(N)]

v = [[0] * N for _ in range(N)]

def bfs(x):
    q = deque()
    q.append(x)
    check = [0 for _ in range(N)]

    while q:
        a = q.popleft()

        for i in range(N):
            if check[i] == 0 and g[a][i] == 1:
                q.append(i)
                check[i] = 1
                v[x][i] = 1

for i in range(0, N):
    bfs(i)

for i in v:
    print(*i)