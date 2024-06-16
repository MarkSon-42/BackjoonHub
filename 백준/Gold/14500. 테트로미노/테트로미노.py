n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
TETROMINO = [
     [(0,0), (0,1), (1,0), (1,1)], 
    [(0,0), (0,1), (0,2), (0,3)], 
    [(0,0), (1,0), (2,0), (3,0)], 
    [(0,0), (0,1), (0,2), (1,0)], 
    [(1,0), (1,1), (1,2), (0,2)],
    [(0,0), (1,0), (1,1), (1,2)], 
    [(0,0), (0,1), (0,2), (1,2)], 
    [(0,0), (1,0), (2,0), (2,1)],
    [(2,0), (2,1), (1,1), (0,1)],
    [(0,0), (0,1), (1,0), (2,0)], 
    [(0,0), (0,1), (1,1), (2,1)],
    [(0,0), (0,1), (0,2), (1,1)], 
    [(1,0), (1,1), (1,2), (0,1)], 
    [(0,0), (1,0), (2,0), (1,1)], 
    [(1,0), (0,1), (1,1), (2,1)], 
    [(1,0), (2,0), (0,1), (1,1)],
    [(0,0), (1,0), (1,1), (2,1)],
    [(1,0), (0,1), (1,1), (0,2)],
    [(0,0), (0,1), (1,1), (1,2)]
]

def find(x, y):
    max_value = 0
    for i in range(19):
        result = 0
        for dx, dy in TETROMINO[i]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m:
                result += board[nx][ny]
            else:
                break
        else:
            max_value = max(max_value, result)
    return max_value

def solve():
    max_value = 0
    for i in range(n):
        for j in range(m):
            max_value = max(max_value, find(i, j))
    return max_value

print(solve())