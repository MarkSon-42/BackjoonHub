i = 1
while True:
    s = ''
    n0 = int(input())
    if n0 == 0:
        break
    else:
        n1 = 3*n0
        if n1 % 2 == 0:
            s = 'even'
            n2 = n1 // 2
        else:
            s = 'odd'
            n2 = (n1 + 1) // 2
    n3 = 3*n2
    n4 = n3 // 9

    print(f'{i}. {s} {n4}')
    i += 1