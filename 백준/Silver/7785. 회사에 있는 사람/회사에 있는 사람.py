n = int(input())

log = {}
for _ in range(n):
    name, enter_log = map(str, input().split())
    log[name] = enter_log

names = []

for key, val in log.items():
    if val == "enter":
        names.append(key)

names.sort(reverse=True)
for n in names:
    print(n)
