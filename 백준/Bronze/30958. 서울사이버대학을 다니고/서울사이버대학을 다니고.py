n = int(input())
songs = input()

alpha = [0 for _ in range(26)]

for c in songs:
    if c == " " or c == "," or c == ".":
        continue
    else:
        alpha[ord(c) % 97] += 1

print(max(alpha))
