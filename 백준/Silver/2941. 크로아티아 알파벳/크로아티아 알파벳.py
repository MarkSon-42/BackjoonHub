s = input()
crots = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

# 2개씩 끊어서 슬라이싱 하면 될듯

for c in crots:
    s = s.replace(c, "#")
print(len(s))

# ljes=njak
# lj e s= nj a k
# e a k

# stack..?
