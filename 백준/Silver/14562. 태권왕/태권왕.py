# c
# s while == t

# 1 . *= 2
# 2.  += 1

# 1번 발차기를 하느냐, 2번 발차기를 하느냐. ->  bfs?

# 1번 예제만 그래프를 그려봐도 bfs로 풀 수 있음을 알 수 있다.

from collections import deque
def bfs(x, y):
    q = deque()
    q.append([x, y, 0])

    while q:
        s, t, cnt = q.popleft()
        if s < t:
            q.append([s * 2, t + 3, cnt + 1])
            q.append([s + 1, t, cnt + 1])
        if s == t:
            print(cnt)
            break

c = int(input())
for _ in range(c):
    s, t = map(int, input().split())
    bfs(s, t)

# bfs 동작시 큐에 들어가고 나오는 순서 (3개씩 s, t, cnt)
#  queue : | 10 | 20 | 0 |  20 |  33 |  1  | 11 | 20 | 1 | 30 | 23 | 2 | 22 | 23 |2 | 23 | 23 | 3