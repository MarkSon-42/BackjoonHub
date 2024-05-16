import sys

sys.setrecursionlimit(10**3)

N, r, c = map(int, input().split())
grid_size = 2**N

def calculate_z_order(row, col, size, value):
    size = size // 2

    if row < size and col < size:
        if size == 1:
            print(value)
            sys.exit(0)
        calculate_z_order(row, col, size, value)

    elif row < size and col >= size:
        if size == 1:
            print(value + 1)
            sys.exit(0)
        calculate_z_order(row, col - size, size, value + size ** 2)

    elif row >= size and col < size:
        if size == 1:
            print(value + 2)
            sys.exit(0)
        calculate_z_order(row - size, col, size, value + size ** 2 * 2)

    elif row >= size and col >= size:
        if size == 1:
            print(value + 3)
            sys.exit(0)
        calculate_z_order(row - size, col - size, size, value + size ** 2 * 3)

calculate_z_order(r, c, grid_size, 0)