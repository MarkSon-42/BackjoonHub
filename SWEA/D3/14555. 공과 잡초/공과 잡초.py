t = int(input())
for tc in range(1, t + 1):
    s = input()
    stack = []
    cnt = 0
    for char in s:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if stack:
                if stack[-1] == '(' or stack[-1] == '|':
                    cnt += 1
                    stack.pop()
        elif char == '|':
            if stack:
                if stack[-1] == '(':
                    cnt += 1
                    stack.pop()
            else:
                stack.append(char)
                
    print(f"#{tc} {cnt}")
                