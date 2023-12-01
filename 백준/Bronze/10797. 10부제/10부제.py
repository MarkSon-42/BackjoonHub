number = int(input())

cars = list(map(int, input().split()))
answer = 0
for i in cars:
    if i != 0 and i % 10 == number:
        answer += 1
    if i == 0 and number == 0:
        answer += 1

print(answer)
