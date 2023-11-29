st = input()
find = input()

stack = []

cnt = 0

for i in st:
    stack.append(i)
    if i == find[-1]:
        if "".join(stack[-len(find):]) == find:
            stack = []
            cnt += 1
print(cnt)