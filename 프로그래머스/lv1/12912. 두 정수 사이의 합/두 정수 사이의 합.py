def solution(a, b):
    answer = 0
    
    d=max(a,b)
    c=min(a,b)
    
    for i in range(c,d+1):
        answer+=i
    
    return answer