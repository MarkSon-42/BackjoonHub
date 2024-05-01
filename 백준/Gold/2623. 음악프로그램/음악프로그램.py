import sys
from collections import deque

input = sys.stdin.readline 

N, M = map(int, input().split())
indegree = [0] * (N + 1)
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    order = list(map(int, input().split()))[1:]
    for i in range(0, len(order) - 1):
        graph[order[i]].append(order[i + 1])
        indegree[order[i + 1]] += 1

queue = deque()

for i in range(1, N + 1):
    if indegree[i] == 0:
        queue.append(i)

result = []

while queue:
    now = queue.popleft()
    result.append(now)
    for i in graph[now]:
        indegree[i] -= 1
        if indegree[i] == 0:
            queue.append(i)

if len(result) == N:
    for i in result:
        print(i)
else:
    print(0)