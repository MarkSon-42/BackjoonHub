T = int(input())
for _ in range(T):
    n = int(input())
    clothes = {}
    for _ in range(n):
        name, category = input().split()
        if category in clothes:
            clothes[category] += 1
        else:
            clothes[category] = 1
            
    ways = 1
    
    for cnt in clothes.values():
        ways *= (cnt + 1)
        
    print(ways - 1)