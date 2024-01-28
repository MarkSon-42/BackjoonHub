N, M = map(int, input().split())
r, c, d = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(N)]

dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]  
room[r][c] = 2  
count = 1

while True:
    check = False
    for _ in range(4):
        d = (d+3) % 4
        nx, ny = r + dx[d], c + dy[d]
        if room[nx][ny] == 0:
            r, c = nx, ny
            room[r][c] = 2
            count += 1
            check = True
            break
    if not check: 
        if room[r-dx[d]][c-dy[d]] == 1: 
            break
        else:
            r, c = r - dx[d], c - dy[d]

print(count)