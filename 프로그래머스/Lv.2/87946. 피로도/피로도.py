from itertools import permutations

def solution(k, dungeons):
    answer = 0
    
    for per in permutations(dungeons):
        limit = k
        cnt = 0
        
        for p in per:
            if limit >= p[0]:
                limit -= p[1]
                cnt += 1
        answer = max(answer, cnt)
        
    return answer
