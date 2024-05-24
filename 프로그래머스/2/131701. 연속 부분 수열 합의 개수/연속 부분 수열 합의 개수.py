def solution(elements):
    n = len(elements)
    elements = elements * 2
    numbers = set()

    for length in range(1, n + 1):
        window_sum = sum(elements[:length])
        numbers.add(window_sum)

        for i in range(length, n + length):
            window_sum = window_sum - elements[i - length] + elements[i]
            numbers.add(window_sum)

    return len(numbers)