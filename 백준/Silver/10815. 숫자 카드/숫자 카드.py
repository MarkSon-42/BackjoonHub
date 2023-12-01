import sys

input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
c = int(input())
cards = list(map(int, input().split()))
nums.sort()

for i in cards:
    answer = 0
    lower_bound = 0
    upper_bound = n - 1

    while lower_bound <= upper_bound:
        mid = (lower_bound + upper_bound) // 2
        if nums[mid] == i:
            answer = 1
            break
        elif i < nums[mid]:
            upper_bound = mid - 1
        else:
            lower_bound = mid + 1
    
    print(answer, end = ' ')