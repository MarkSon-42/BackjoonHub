s = list(input())

rev_s = [s[i] for i in range(len(s) - 1, -1, -1)]

print(1 if s == rev_s else 0)
