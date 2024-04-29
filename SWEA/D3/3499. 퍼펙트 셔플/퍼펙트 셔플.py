from collections import deque


t = int(input())
for tc in range(t):
    n = int(input())
    deq = list(map(str, input().split()))
    half = deque()
    left = deque()
    answer = []
    if n % 2 != 0:
        for i in range(0, n//2 + 1):
            half.append(deq[i])

        for i in range(n//2 + 1, n):
            left.append(deq[i])
    else:
        for i in range(0, n//2):
            half.append(deq[i])

        for i in range(n//2, n):
            left.append(deq[i])

    while half or left:
        if half:
            answer.append(half.popleft())
        if left:
            answer.append(left.popleft())

    print(f'#{tc+1}', ' '.join(answer))