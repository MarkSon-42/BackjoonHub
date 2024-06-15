from collections import deque
import sys

T = int(sys.stdin.readline())
for _ in range(T):
    commands = sys.stdin.readline().strip()
    n = int(sys.stdin.readline())
    arr = sys.stdin.readline().strip()[1:-1].split(',')
    dq = deque(arr if arr[0] else [])
    is_reversed = False

    for command in commands:
        if command == 'R':
            is_reversed = not is_reversed
        elif command == 'D':
            if dq:
                dq.pop() if is_reversed else dq.popleft()
            else:
                print('error')
                break
    else:
        dq = reversed(dq) if is_reversed else dq
        print('[' + ','.join(dq) + ']')