import sys
input = sys.stdin.readline
m=[]
n = int(input())
for _ in range(n):
    m.append(int(input()))
for i in sorted(m):
    print(i)
