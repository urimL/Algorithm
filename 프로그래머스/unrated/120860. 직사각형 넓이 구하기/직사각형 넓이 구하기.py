def solution(dots):
    answer = 0
    
    answer = (max(dots)[0]-min(dots)[0])*(max(dots)[1]-min(dots)[1])
    
    return answer