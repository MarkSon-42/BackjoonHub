from collections import deque

N, M = map(int, input().split())

arr = [[] for _ in range(N+1)]
for i in range(M):
    A, B = map(int, input().split())
    arr[A].append(B)
    arr[B].append(A)

def bfs(start):
    visited = [-1] * (N + 1)

    q = deque()
    q.append(start)
    visited[start] = 0

    while q:
        node = q.popleft()

        for next_node in arr[node]:
            if visited[next_node] == -1:
                visited[next_node] = visited[node] + 1
                q.append(next_node)
    return sum(visited)

min_total = float("INF")
answer = 0
for i in range(1, N+1):

    total = bfs(i)
    if total < min_total:
        min_total = total
        answer = i

print(answer)