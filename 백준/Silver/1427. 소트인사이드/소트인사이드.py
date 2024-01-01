n = []
string = ""
num = input()
for c in num:
    n.append(int(c))
answer = sorted(n, reverse=True)
for i in answer:
    string += str(i)

print(string)
