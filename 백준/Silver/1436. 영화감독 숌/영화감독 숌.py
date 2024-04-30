n = int(input())
cnt = 0
answer = 666

while 1:
    if '666' in str(answer):
        cnt += 1

    if cnt == n:
        break

    answer += 1

print(answer)