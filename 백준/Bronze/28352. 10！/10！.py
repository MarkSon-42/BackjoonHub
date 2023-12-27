n = int(input())


def fact(x):
    if x == 1:
        return 1
    else:
        return fact(x - 1) * x


print(fact(n) // (3628800 // 6))
