def count_stars(N):
    num_stars = (N * (N - 1) * (N - 2) * (N - 3) * (N - 4)) // 120
    return num_stars


N = int(input())

print(count_stars(N))
