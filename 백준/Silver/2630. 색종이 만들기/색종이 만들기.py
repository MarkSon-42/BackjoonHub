N = int(input())
g = [list(map(int, input().split())) for _ in range(N)]

b = 0
w = 0

def sol(x, y, N):
    global w, b
    color = g[x][y]
    for i in range(x, x + N):
        for j in range(y, y + N):
            if color != g[i][j]:
                sol(x, y, N // 2)
                sol(x, y + N // 2, N // 2)
                sol(x + N // 2, y, N // 2)
                sol(x + N // 2, y + N // 2, N // 2)
                return
    if color == 0:
        w += 1
    else:
        b += 1

sol(0, 0, N)
print(w)
print(b)