
def dfs(n, sm):
    global answer
    # 1. 종료 조건 : 가능한 n을 종료에 관련된 것으로 정의!
    if n >= N:
        answer = max(answer, sm)
        return

    # 2. 하부 호출 : 화살표 개수 만큼 호출

    # 2 - 1 : 상담 하는 경우
    if n + T[n] <= N:
        dfs(n + T[n], sm + P[n])

    # 가능한 모든 경우를 해보는 것이다.
    # 여기서 습관적으로 else를 쓰면 망한다.

    # 2 - 2 : 상담하지 않는 경우
    dfs(n + 1, sm)


N = int(input())
T = [0] * N
P = [0] * N
for i in range(N):
    T[i], P[i] = map(int, input().split())

answer = 0
dfs(0, 0)
print(answer)