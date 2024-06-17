S = input()
suffixes = [S[i:] for i in range(len(S))]
for suffix in sorted(suffixes):
    print(suffix)