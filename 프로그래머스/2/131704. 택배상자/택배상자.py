from collections import deque

def solution(order):
    main_belt = deque([i for i in range(1, len(order) + 1)])
    sub_belt = []
    counter = 0
    idx = 0

    while main_belt:
        if order[idx] == main_belt[0]:
            main_belt.popleft()
            counter += 1
            idx += 1
        else:
            sub_belt.append(main_belt.popleft())

        while sub_belt and order[idx] == sub_belt[-1]:
            sub_belt.pop()
            counter += 1
            idx += 1

    return counter