def solution(pgs, speeds):
    answer = []
    
    while pgs:
        cnt = 0
        
        while pgs and pgs[0] >= 100:
            cnt += 1
            pgs.pop(0)
            speeds.pop(0)
            
        for i in range(len(pgs)):
            pgs[i] += speeds[i]
        
        if cnt:
            answer.append(cnt)
    return answer