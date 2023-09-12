def solution(n, lost, reserve):
    answer=0
    lost.sort()
    
    for i in range(1,n+1):
        #잃어버리지 않은 학생
        if i not in lost:
            answer+=1
        #잃어버렸으나 여분이 있는 학생
        else:
            if i in reserve:
                answer+=1
                lost.remove(i)
                reserve.remove(i)
    
    for i in lost:
        if i-1 in reserve:
            answer+=1
            reserve.remove(i-1)
            
        elif i+1 in reserve:
            answer+=1
            reserve.remove(i+1)
        
    return answer
