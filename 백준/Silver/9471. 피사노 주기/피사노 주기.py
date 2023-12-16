#  첫째 줄에 n이 주어진다. n은 1,000,000,000,000,000,000보다 작거나 같은 자연수이다.
#
# def fibo_recur(n):
#     if n == 0:
#         return 0
#     elif n <= 2:
#         return 1
#     else:
#         return fibo_recur(n - 1) + fibo_recur(n - 2)
#
# n = int(input())
# print(fibo_recur(n) % 1000000)
#
#
# def fibo_memo(x):
#     dp = [0] * (x + 1)
#     dp[1] = 1
#     dp[2] = 2
#     for i in range(3, x + 1):
#         dp[i] = dp[i - 1] + dp[i - 2]
#
#     return dp[x] % 1000000
#
#
# n = int(input())
# print(fibo_memo(n))

# boj 9471 passano


def pisano(n):
    answer = 1
    mod1, mod2 = 1, 2
    while True:
        if mod1 % n == 1 and mod2 % n == 1:
            break
        answer += 1
        mod1, mod2 = mod2, (mod1 + mod2) % n

    return answer


p = int(input())

for _ in range(p):
    n, m = map(int, input().split())
    answer = pisano(m)

    print(f"{n} {answer}")
