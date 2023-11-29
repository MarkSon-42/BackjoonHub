import sys

input = sys.stdin.readline

n = int(input())

building = [int(input()) for _ in range(n)]
stack = []
answer = 0

for i in range(n):
    while stack and stack[-1] <= building[i]:
        stack.pop()

    stack.append(building[i])
    answer += len(stack) - 1

print(answer)
