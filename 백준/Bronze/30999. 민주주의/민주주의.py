answer = 0
n, m = map(int, input().split())
for _ in range(n):
    votes = input()
    cnt = votes.count("O")

    if cnt > (m // 2):
        answer += 1

print(answer)
