import sys
from collections import deque

# 표준 입력을 빠르게 받기 위한 설정
input = sys.stdin.readline

# 격자의 높이 n과 너비 m을 입력받음
n, m = map(int, input().split())

# n개의 줄에 걸쳐 각 줄마다 m개의 숫자를 입력받아 2차원 리스트 grid를 생성
grid = [list(map(int, input().rstrip())) for _ in range(n)]

# 상, 하, 좌, 우 방향을 나타내는 리스트
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 너비 우선 탐색(BFS) 함수 정의
def bfs(x, y):
    # deque 생성
    q = deque()
    # 시작점을 큐에 추가
    q.append((x, y))
    
    # 큐가 빌 때까지 반복
    while q:
        x, y = q.popleft()
        
        # 네 방향에 대해
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            # 새로운 위치가 격자 내에 있고, 아직 방문하지 않은 셀이라면
            if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == 1:
                # 셀을 방문했다고 표시하고
                q.append((nx, ny))
                # 셀을 방문한 횟수를 증가
                grid[nx][ny] = grid[x][y] + 1
            
    # 마지막 셀까지의 최단 거리를 반환
    return grid[n - 1][m - 1]

# 시작점에서 BFS를 시작하고 결과를 출력
print(bfs(0, 0))