from collections import defaultdict

def solve():
    N = int(input())
    S = list(map(int, input().split()))
    count = defaultdict(int)
    max_length = 0
    j = 0

    for i in range(N):
        while j < N and len(count) <= 2:
            count[S[j]] += 1
            if len(count) <= 2:
                max_length = max(max_length, j - i + 1)
            j += 1
        count[S[i]] -= 1
        if count[S[i]] == 0:
            del count[S[i]]
    return max_length

print(solve())