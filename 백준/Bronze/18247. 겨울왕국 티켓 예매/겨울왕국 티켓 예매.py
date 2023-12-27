# L4, 즉 L열의 네 번째 자리에 앉으려고 한다.
# 영화관은 세로로 N칸, 가로로 M칸인 좌석들로 구성
#
#
# ABCDEFGHIJKL
# 1234567891011
t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    if n < 12:
        print(-1)
        continue
    if m < 4:
        print(-1)
        continue
    else:
        print(11 * m + 4)
