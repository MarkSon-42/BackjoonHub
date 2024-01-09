# 롤러가 벽에서 벗어나면 안 됩니다.
# 구역의 일부분만 포함되도록 칠하면 안 됩니다.

def solution(n, m, section):
    answer = 0
    while section:  
        left = section[0]  # 6
        right = section[0] + m  # 10
        while section and section[0] < right:
            del section[0]
        answer += 1
    return answer  # 2