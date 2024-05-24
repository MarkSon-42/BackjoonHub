def solution(elements):
    
    # 원형 수열을 만들기 위해 elements를 두 번 복사
    
    elements = elements * 2
    l = len(elements) // 2
    numbers = set()

    for i in range(l):
        for j in range(1, l + 1):
            numbers.add(sum(elements[i:i+j]))

    return len(numbers)