while True:
    s = input()
    if s == '.':
        break

    stack = []
    balanced = True
    for char in s:
        if char in ('(', '['):
            stack.append(char)
        elif char == ')':
            if not stack or stack[-1] != '(':
                balanced = False
                break
            stack.pop()
        elif char == ']':
            if not stack or stack[-1] != '[':
                balanced = False
                break
            stack.pop()

    if balanced and not stack:
        print('yes')
    else:
        print('no')