s = input().split('-')

total_sum = 0

for number in s[0].split('+'):
    total_sum += int(number)

for element in s[1:]:
    for number in element.split('+'):
        total_sum -= int(number)

print(total_sum)