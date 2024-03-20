sum = 0
for _ in range(5):
    n = int(input())
    if n >= 40:
        sum += n
    else:
        sum += 40

print(sum//5)
