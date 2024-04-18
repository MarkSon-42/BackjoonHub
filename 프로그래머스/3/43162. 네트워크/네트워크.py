from collections import deque

def solution(n, computers):
    visited = [False] * n
    answer = 0

    for i in range(n):
        if not visited[i]:
            queue = deque([i])
            while queue:
                node = queue.popleft()
                visited[node] = True
                for idx, is_connected in enumerate(computers[node]):
                    if is_connected and not visited[idx]:
                        queue.append(idx)
            answer += 1
    return answer