a, b = input().split()
a = list(a)
a.reverse()
b = list(b)
b.reverse()
a = int("".join(a))
b = int("".join(b))

print(a if a > b else b)
