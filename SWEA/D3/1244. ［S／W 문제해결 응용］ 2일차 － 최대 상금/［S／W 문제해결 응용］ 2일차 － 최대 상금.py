
def dfs(n):
    global answer
    if n == N:
        answer = max(answer, int("".join(map(str, lst))))
        return

    # L개에서 2개 뽑는 모든 조합
    for i in range(L - 1):
        for j in range(i + 1, L):
            lst[i], lst[j] = lst[j], lst[i]

            chk = int("".join(map(str, lst)))
            if (n, chk) not in visited:
                dfs(n + 1)
                visited.append((n, chk))
            lst[i], lst[j] = lst[j], lst[i]

T = int(input())
for tc in range(1, T + 1):
    s, t = input().split()
    N = int(t)
    lst = []
    for char in s:
        lst.append(int(char))

    L = len(lst)
    answer = 0

    visited = []
    dfs(0)

    print(f'#{tc} {answer}')
