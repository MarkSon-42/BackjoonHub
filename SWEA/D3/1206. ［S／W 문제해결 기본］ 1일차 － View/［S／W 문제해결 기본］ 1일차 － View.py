# 쪽과 오른쪽으로 창문을 열었을 때, 양쪽 모두 거리 2 이상의 공간이 확보될 때 조망권이 확보된다

#  조망권이 확보된 세대의 수를 반환하는 프로그램을 작성


tc = 10

for t in range(1, tc + 1):
    n = int(input())
    building = list(map(int, input().split()))
    answer = 0

    for i in range(2, n - 2):
        if ((building[i - 2] < building[i] and building[i - 1] < building[i])
                and (building[i + 1] < building[i] and building[i + 2] < building[i])):
            answer += building[i] - max(building[i - 2], building[i - 1], building[i + 1], building[i + 2])
    print(f"#{t} {answer}")