n = int(input())
bus = dict()
answer = 0

for _ in range(n):
    city, price = input().split()
    bus[city] = int(price)

filtered = filter(lambda e: e[1] > bus["jinju"], bus.items())
new_dict = dict(filtered)
print(bus["jinju"])
print(len(new_dict))
