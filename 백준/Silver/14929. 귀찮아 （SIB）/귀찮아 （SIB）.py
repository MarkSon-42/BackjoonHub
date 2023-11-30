n = int(input())

x = list(map(int, input().split()))

num = [x[0]]

for i in range(1, n):
    num.append(num[i-1] + x[i])
    
answer = 0 

for i in range(n):
    answer += x[i] * (num[n - 1] - num[i])
    
print(answer)