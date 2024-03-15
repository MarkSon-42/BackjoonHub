t = int(input())

for _ in range(t):
    n = int(input())
    schools = set()
    for i in range(n):
        school_name, drink = map(str, input().split())
        drink = int(drink)
        schools.add((drink, school_name))
        
    print(max(schools)[1])
        