def recur(n, m):
    if m == 0:
        return 1
    else:
        return n * recur(n, m - 1)
        
t = 10
for tc in range(1, t + 1):
    testcase = int(input())
    n, m = map(int, input().split())
    
    answer = recur(n, m)
    
    print(f"#{tc} {answer}")
    