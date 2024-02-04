n = int(input())
arr = "".join(str(i) for i in range(1, n + 1))

index = arr.find(str(n))
print(index + 1)