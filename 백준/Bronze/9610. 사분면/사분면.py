n = int(input())
counters = {'Q1': 0, 'Q2': 0, 'Q3': 0, 'Q4': 0, 'AXIS': 0}

for _ in range(n):
    x, y = map(int, input().split())
    if x == 0 or y == 0:
        counters['AXIS'] += 1
    elif x > 0 and y > 0:
        counters['Q1'] += 1
    elif x < 0 and y > 0:
        counters['Q2'] += 1
    elif x < 0 and y < 0:
        counters['Q3'] += 1
    elif x > 0 and y < 0:
        counters['Q4'] += 1

for quadrant, count in counters.items():
    print(f'{quadrant}: {count}')