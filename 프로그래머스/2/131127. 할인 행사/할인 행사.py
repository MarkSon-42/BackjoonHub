def solution(want, number, discount):
    answer = 0
    
    for i in range(len(discount) - 9):
        can_buy = True
        for j in range(len(want)):
            if discount[i:i+10].count(want[j]) < number[j]:
                can_buy = False
                break
        if can_buy:
            answer += 1
    
    return answer