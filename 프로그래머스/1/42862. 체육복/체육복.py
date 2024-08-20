def solution(n, lost, reserve):
    
    answer = n - len(lost)
    extra = [False]*(n+2)
    result = [True] * (n+2)
    result[0], result[-1] = False, False
    lost.sort()
    
    for r in reserve:
        extra[r] = True
    
    for l in lost:
        if extra[l]:
            extra[l] = False
            answer += 1
        else:
            result[l] = False
            
    for l in lost:
        if extra[l]:
            answer += 1
            extra[l] = False
        
    for l in lost:
        if not result[l]:
            if extra[l-1]:
                extra[l-1] = False
                answer += 1
            elif extra[l+1]:
                extra[l+1] = False
                answer += 1 
    
    return answer