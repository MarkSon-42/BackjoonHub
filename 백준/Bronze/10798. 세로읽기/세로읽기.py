lines = [input() for _ in range(5)]
lengths = [len(line) for line in lines]
ans = ''

for j in range(max(lengths)):
    for i in range(5):
        if j < lengths[i]:
            ans += lines[i][j]

print(ans)