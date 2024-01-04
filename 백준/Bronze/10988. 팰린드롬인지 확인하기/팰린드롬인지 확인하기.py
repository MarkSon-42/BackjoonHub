s = input()
s = list(s)

rev_s = []
for i in range(len(s) - 1, -1, -1):
    rev_s.append(s[i])

print(1 if s == rev_s else 0)
