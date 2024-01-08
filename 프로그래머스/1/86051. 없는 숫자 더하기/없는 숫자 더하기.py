def solution(numbers):
    answer = 0
    number_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    for n in number_list:
        if n not in numbers:
            answer += n
    return answer