def check_string(s):
    stack = []
    matching_bracket = {')': '(', ']': '[', '}': '{'}
    for char in s:
        if char in '({[':
            stack.append(char)
        elif char in ')}]':
            if not stack or stack[-1] != matching_bracket[char]:
                return False
            stack.pop()
    return not stack

def solution(s):
    valid_count = 0
    n = len(s)

    for i in range(n):
        rotated_s = s[i:] + s[:i]
        if check_string(rotated_s):
            valid_count += 1

    return valid_count


