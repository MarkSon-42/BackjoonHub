t = int(input())

for _ in range(t):
    n = int(input())
    max_drink = 0
    max_school = ""
    for i in range(n):
        school_name, drink = map(str, input().split())
        drink = int(drink)
        if drink > max_drink:
            max_drink = drink
            max_school = school_name
    print(max_school)
        
