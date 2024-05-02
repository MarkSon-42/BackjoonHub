def get_pi(pattern):
    m = len(pattern)
    j = 0
    pi = [0] * m
    for i in range(1, m):
        while j > 0 and pattern[i] != pattern[j]:
            j = pi[j - 1]
        if pattern[i] == pattern[j]:
            j += 1
            pi[i] = j
    return pi

L = int(input())
S = input().strip()
pi = get_pi(S)
print(L - pi[L - 1])