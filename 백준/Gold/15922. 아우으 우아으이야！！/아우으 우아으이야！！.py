num = int(input())

start, end = map(int, input().split())

total = 0

for i in range(num - 1):
    next_start, next_end = map(int, input().split())
    if next_start == start:
        end = next_end
    elif end >= next_start and next_end > end:
        end = next_end
    elif end < next_start:
        total += abs(start - end)
        start = next_start
        end = next_end

print(total + abs(end - start))