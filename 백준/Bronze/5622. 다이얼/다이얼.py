answer = 0
dial = ["ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"]

string = input()

for c in string:
    answer += 2
    for i in range(len(dial)):
        if c in dial[i]:
            answer += i + 1

print(answer)
