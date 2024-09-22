# arr 1,000,000
# 인접한 동일 요소 중복 제거 -> stack!

def solution(arr):
    stack = []
    for i in range(len(arr)):
        if not stack or stack[-1] != arr[i]:
            stack.append(arr[i])
    return stack