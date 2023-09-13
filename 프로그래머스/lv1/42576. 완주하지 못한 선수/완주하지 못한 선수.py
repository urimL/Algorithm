def solution(participant, completion):
    sumHash=0
    tmp={}
    
    for i in participant:        
        tmp[hash(i)] = i
        sumHash += hash(i)
            
    for i in completion:
        sumHash-=hash(i)
    
    return tmp[sumHash]
