
T = int(input())
for t in range(1, T+1):
    numbers = list(map(int, input().split()))
    numbers.remove(max(numbers))
    numbers.remove(min(numbers))
    average = round(sum(numbers) / len(numbers))
    print(f'#{t} {average}')