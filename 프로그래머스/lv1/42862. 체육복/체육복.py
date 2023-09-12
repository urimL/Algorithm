def solution(n, lost, reserve):
    answer=n-len(lost)
    lost.sort()
    
    for i in lost:
        if i in reserve:
            answer+=1
            lost[lost.index(i)]=-10
            reserve[reserve.index(i)] =-10
    
    for i in lost:
        if i-1 in reserve:
            answer+=1
            reserve[reserve.index(i-1)] = -10
            continue
            
        if i+1 in reserve:
            answer+=1
            reserve[reserve.index(i+1)] = -10
            continue
        
    return answer