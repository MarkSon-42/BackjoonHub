
while True:
    a, b, c = map(int, input().split())
    if a == 0 and b == 0 and c == 0:
        exit(0)
    if a + b <= c or b + c <= a or a + c <= b:
        print('Invalid')
        continue

    if a == b == c:
        print('Equilateral')
    elif a == b and b != c:
        print('Isosceles')
    elif a != b and b == c:
        print('Isosceles')
    elif a == c and b != c:
        print('Isosceles')
    elif a != b and b != c and c != a:
        print('Scalene')
    else:
        pass

