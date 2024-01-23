from collections import deque

def solution(x, y, n):
    queue = deque([(x, 0)]) 
    visited = {x} 

    while queue:
        current, operations = queue.popleft()

        if current == y:
            return operations

        for next_num in [current + n, current * 2, current * 3]:
            if next_num not in visited and next_num <= y:
                queue.append((next_num, operations + 1))
                visited.add(next_num)

    return -1