def solution(elements):
    l = len(elements)
    elements = elements * 2
    answer = set()

    for i in range(1, l + 1):
        window_sum = sum(elements[:i])
        answer.add(window_sum)

        for j in range(i, l + i):
            window_sum = window_sum - elements[j - i] + elements[j]
            answer.add(window_sum)

    return len(answer)