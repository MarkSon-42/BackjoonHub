import sys

N, M = map(int, sys.stdin.readline().split())

name_to_num = {}
num_to_name = {}

for i in range(1, N+1):
    name = sys.stdin.readline().strip()
    name_to_num[name] = i
    num_to_name[i] = name

for i in range(M):
    question = sys.stdin.readline().strip()
    if question[0].isalpha():
        print(name_to_num[question])  # 이름으로 번호 찾기
    else:
        print(num_to_name[int(question)])  # 번호로 이름 찾기