n = int(input())
m = int(input())
lights = list(map(int, input().split()))

max_size = 0
for i in range(1, m):
    max_size = max(max_size, lights[i] - lights[i - 1])
    
print(max((max_size + 1) // 2, lights[0] - 0, n - lights[-1]))