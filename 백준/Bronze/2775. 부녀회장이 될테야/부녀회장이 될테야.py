T = int(input())
for _ in range(T):
    k = int(input())
    n = int(input())
    residents = [[0 for _ in range(n+1)] for _ in range(k+1)]
    for i in range(n+1):
        residents[0][i] = i
    for i in range(1, k+1):
        for j in range(1, n+1):
            residents[i][j] = residents[i-1][j] + residents[i][j-1]
    print(residents[k][n])