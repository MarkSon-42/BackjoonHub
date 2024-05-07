s = [sum(map(int, input().split())) for _ in range(5)]
w = s.index(max(s)) + 1
print(w, max(s))