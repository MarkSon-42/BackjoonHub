import math

A, B, V = map(int, input().split())
days = (V - B) / (A - B)

print(math.ceil(days))