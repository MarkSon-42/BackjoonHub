import sys
from collections import Counter

n = int(sys.stdin.readline())
numbers = [int(sys.stdin.readline()) for _ in range(n)]

# 평균
mean = round(sum(numbers) / n)

# 중간값, 중앙값
numbers.sort()
median = numbers[n // 2]


counts = Counter(numbers)
modes = [k for k, v in counts.items() if v == max(counts.values())]
modes.sort()
mode = modes[0] if len(modes) == 1 else modes[1]


range_ = max(numbers) - min(numbers)

print(mean)
print(median)
print(mode)
print(range_)