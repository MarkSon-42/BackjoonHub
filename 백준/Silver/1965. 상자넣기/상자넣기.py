n = int(input())
box = list(map(int, input().split()))
dp = [0 for _ in range(n + 1)]
dp[0] = 0
dp[1] = 1

# 상자에 넣는 방법이 여러가지인데 그 중에서 최대의 상자 개수를 출력해야 한다.

# 그러면 dp = max(dp[i], dp[j] + 1) 이런 형태의 점화식일 가능성이 높다.

# dp[i]는 i번째 상자까지 넣을 수 있는 최대의 상자 개수를 의미한다.

# dp[j] + 1은 j번째 상자까지 넣을 수 있는 최대의 상자 개수에 1을 더한 것이다.

# 그러면 dp[i]는 dp[j] + 1 중에서 최대값을 가지게 된다.

# 그러면 dp[i] = max(dp[i], dp[j] + 1) 이런 형태의 점화식이 나온다.

# 그러면 j는 i보다 작아야 한다. 왜냐하면 i번째 상자는 j번째 상자보다 크기가 커야 하기 때문이다.

# 그러면 j는 1부터 i - 1까지의 범위를 가지게 된다.

# 그러면 점화식은 dp[i] = max(dp[i], dp[j] + 1) (1 <= j < i) 이런 형태가 된다.

# 그러면 코드는 다음과 같다.

for i in range(2, n + 1):
    for j in range(1, i):
        if box[i - 1] > box[j - 1]:
            dp[i] = max(dp[i], dp[j] + 1)
        else:
            dp[i] = max(dp[i], 1)
        
print(max(dp))

# 이렇게 하면 시간 초과가 나온다.