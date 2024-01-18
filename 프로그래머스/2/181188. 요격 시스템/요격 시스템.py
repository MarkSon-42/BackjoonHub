def solution(targets):
    targets.sort(key=lambda x: (x[1], x[0]))

    cut = -1
    answer = 0

    for left, right in targets:
        if left >= cut:
            answer += 1
            cut = right

    return answer
