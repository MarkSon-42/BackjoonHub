def solution(d, budget):
    answer = 0
    d = sorted(d)
    for dep in d:
        if budget - dep >= 0:
            answer += 1
            budget -= dep
        else:
            break

    return answer