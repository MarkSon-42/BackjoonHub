N, M = map(int, input().split())
r, c, d = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(N)]

dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]  # North, East, South, West
cleaned = [[0]*M for _ in range(N)]
cleaned[r][c] = 1  # Start cell is cleaned
count = 1

while True:
    check = False
    for _ in range(4):
        d = (d+3) % 4  # Rotate to left
        nx, ny = r + dx[d], c + dy[d]
        if room[nx][ny] == 0 and cleaned[nx][ny] == 0:  # If the cell is not cleaned
            r, c = nx, ny
            cleaned[r][c] = 1
            count += 1
            check = True
            break
    if not check:  # If all cells around are cleaned or wall
        if room[r-dx[d]][c-dy[d]] == 1:  # If the backward cell is wall
            break
        else:
            r, c = r - dx[d], c - dy[d]

print(count)