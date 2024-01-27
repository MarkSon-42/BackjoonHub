import sys

s = input()
bomb = input()
stack = []
bomb_length = len(bomb)

for char in s:
    stack.append(char)
    if "".join(stack[-bomb_length:]) == bomb:
        del stack[-bomb_length:]

print("".join(stack) if stack else "FRULA")
