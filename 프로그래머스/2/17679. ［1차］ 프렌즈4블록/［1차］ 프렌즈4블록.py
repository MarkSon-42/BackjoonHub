def solution(m, n, board):
    board = [list(x) for x in board]
    answer = 0

    while True:
        to_remove = set()
        for i in range(m-1):
            for j in range(n-1):
                if board[i][j] == board[i][j+1] == board[i+1][j] == board[i+1][j+1] != '_':
                    to_remove |= {(i, j), (i, j+1), (i+1, j), (i+1, j+1)}

        if not to_remove:
            return answer

        answer += len(to_remove)
        for i, j in to_remove:
            board[i][j] = '_'

        for _ in range(m):
            for i in range(m-1):
                for j in range(n):
                    if board[i+1][j] == '_':
                        board[i+1][j], board[i][j] = board[i][j], '_'