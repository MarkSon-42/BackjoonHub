k = int(input())
stack = []
for _ in range(k):
    s = int(input())
    if s != 0:
        stack.append(s)
    else:
        stack.pop()
print(sum(stack))
