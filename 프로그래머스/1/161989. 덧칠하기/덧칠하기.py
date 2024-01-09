# 조건문과 반복문의 기초적인 활용을 묻는 문제라고 생각.

def solution(n, m, section):
    answer = 0
    while section:
        left = section[0]
        right = left + m
        while section and section[0] < right:
            del section[0]
        answer += 1
    return answer