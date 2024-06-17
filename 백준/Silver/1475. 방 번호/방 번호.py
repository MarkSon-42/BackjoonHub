import math

room_number = input().strip()
counts = [0] * 10

for num in room_number:
    counts[int(num)] += 1

counts[6] = math.ceil((counts[6] + counts[9]) / 2)
counts[9] = 0

print(max(counts))