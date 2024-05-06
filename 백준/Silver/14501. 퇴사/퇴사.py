n = int(input())
t = [] # 상담 기간
p = [] # 상담 비용
max_profit = 0 # 최대 이익

for i in range(n):
    ti, pi = map(int, input().split())
    t.append(ti)
    p.append(pi)

def backtrack(day, profit):
    global max_profit
    
    # N+1번째 날짜에는 상담을 할 수 없음
    if day == n+1:
        max_profit = max(max_profit, profit)
        return
    
    # 상담을 하는 경우
    if day + t[day-1] <= n+1:
        backtrack(day + t[day-1], profit + p[day-1])
    
    # 상담을 하지 않는 경우
    backtrack(day + 1, profit)

backtrack(1, 0)
print(max_profit)
