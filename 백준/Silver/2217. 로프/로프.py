N = int(input())

ropes = [int(input())for _ in range(N)]
ropes.sort()

answers = []
for x in ropes:
    answers.append(x * N)
    N -= 1
print(max(answers))