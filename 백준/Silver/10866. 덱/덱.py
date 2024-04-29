from collections import deque
import sys

def push_front(X):
    deque.appendleft(X)

def push_back(X):
    deque.append(X)

def pop_front():
    return deque.popleft() if deque else -1

def pop_back():
    return deque.pop() if deque else -1

def size():
    return len(deque)

def empty():
    return 0 if deque else 1

def front():
    return deque[0] if deque else -1

def back():
    return deque[-1] if deque else -1

N = int(sys.stdin.readline().rstrip())
deque = deque()

for _ in range(N):
    command = sys.stdin.readline().rstrip().split()

    if command[0] == "push_front":
        push_front(int(command[1]))
    elif command[0] == "push_back":
        push_back(int(command[1]))
    elif command[0] == "pop_front":
        print(pop_front())
    elif command[0] == "pop_back":
        print(pop_back())
    elif command[0] == "size":
        print(size())
    elif command[0] == "empty":
        print(empty())
    elif command[0] == "front":
        print(front())
    elif command[0] == "back":
        print(back())