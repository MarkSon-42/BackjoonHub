N, M = map(int, input().split())
not_heard = set()
not_seen = set()

for _ in range(N):
    not_heard.add(input().strip())

for _ in range(M):
    not_seen.add(input().strip())

not_heard_seen = sorted(list(not_heard & not_seen))

print(len(not_heard_seen))
for name in not_heard_seen:
    print(name)