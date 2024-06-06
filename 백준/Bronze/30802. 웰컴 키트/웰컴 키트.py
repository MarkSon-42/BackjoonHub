import math

N = int(input())
S, M, L, XL, XXL, XXXL = map(int, input().split())
T, P = map(int, input().split())

shirt_sizes = [S, M, L, XL, XXL, XXXL]

shirt_bundles = sum(math.ceil(size / T) for size in shirt_sizes)
pen_bundles = N // P
pen_singles = N % P

print(shirt_bundles)
print(pen_bundles, pen_singles)