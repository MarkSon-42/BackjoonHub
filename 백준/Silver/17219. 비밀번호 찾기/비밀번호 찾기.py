N, M = map(int, input().split())

notepad = {}

for i in range(N):
    domain, pw = input().split()
    notepad[domain] = pw

for i in range(M):
    s = input()
    if s in notepad:
        print(notepad[s])