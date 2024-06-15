from collections import deque
import sys

input = sys.stdin.readline

def apply_operation(number, operation):
    if operation == "D":
        return (number * 2) % 10000
    elif operation == "S":
        return (number - 1) % 10000
    elif operation == "L":
        return (10 * number + (number // 1000)) % 10000
    elif operation == "R":
        return (((number % 10) * 1000) + (number // 10)) % 10000

def bfs(start):
    queue = deque()
    queue.append((start, ""))
    visited = [False] * 10000
    visited[start] = True

    while queue:
        number, result = queue.popleft()

        if number == target:
            return result

        for operation in operations:
            new_number = apply_operation(number, operation)

            if not visited[new_number]:
                visited[new_number] = True
                queue.append((new_number, result + operation))

test_cases = int(input())
operations = ["D", "S", "L", "R"]

for _ in range(test_cases):
    start, target = map(int, input().split())
    print(bfs(start))