import sys

input = sys.stdin.readline

n = int(input())

num_list = list(map(int, input().split()))
# [1000, 999, 1000, 999]

temp = list(set(num_list))  # [1000, 999]

temp.sort()  # [999, 1000]

number_dict = dict()  # {}

# 아래 라인부터는 특정 테스트케이스에 대해서 동작을 적어보던지 해야함 _ debugger로는 충분치 않음.

for i in range(len(temp)):
    number_dict[temp[i]] = i


for j in num_list:
    print(number_dict[j], end=" ")
