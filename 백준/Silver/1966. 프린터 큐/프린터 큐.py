from collections import deque

for _ in range(int(input())):
    n, m = map(int, input().split())
    queue = deque(map(int, input().split()))
    idx = deque(range(n))

    order = 0

    while True:
        if queue[0] == max(queue):
            order += 1
            if idx[0] == m:
                print(order)
                break
            else:
                queue.popleft()
                idx.popleft()
        else:
            queue.append(queue.popleft())
            idx.append(idx.popleft())