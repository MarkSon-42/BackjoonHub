# 복잡도를 신경써야 한다

# 탐색의 범위를 좀 줄여야 할것

# 즉, 작은 값부터 시작해서 0부터 인덱스를 부여하는 방식

import sys

input = sys.stdin.readline
n = int(input())

num_list = list(map(int, input().split()))

temp = list(set(num_list))

temp.sort()

number_dict = dict()

for i in range(len(temp)):
    number_dict[temp[i]] = i

for j in num_list:
    print(number_dict[j], end=" ")
